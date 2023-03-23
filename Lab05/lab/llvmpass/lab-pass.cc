/*
  Ref:
  * https://llvm.org/doxygen/
  * https://llvm.org/docs/GettingStarted.html
  * https://llvm.org/docs/WritingAnLLVMPass.html
  * https://llvm.org/docs/ProgrammersManual.html
 */
#include "lab-pass.h"
#include "llvm/IR/LegacyPassManager.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/BasicBlock.h"
#include "llvm/IR/IRBuilder.h"
#include "llvm/IR/Constants.h"

using namespace llvm;

char LabPass::ID = 0;

static Constant* getI8StrVal(Module &M, char const *str, Twine const &name) {
  LLVMContext &ctx = M.getContext();
  Constant *strConstant = ConstantDataArray::getString(ctx, str);
  GlobalVariable *gvStr = new GlobalVariable(M, strConstant->getType(), true,
    GlobalValue::InternalLinkage, strConstant, name);
  Constant *zero = Constant::getNullValue(IntegerType::getInt32Ty(ctx));
  Constant *indices[] = { zero, zero };
  Constant *strVal = ConstantExpr::getGetElementPtr(Type::getInt8PtrTy(ctx),
    gvStr, indices, true);
  return strVal;
}

static FunctionCallee printfPrototype(Module &M) {
  LLVMContext &ctx = M.getContext();
  FunctionType *printfType = FunctionType::get(
    Type::getInt32Ty(ctx),
    { Type::getInt8PtrTy(ctx) },
    true);
  FunctionCallee printfCallee = M.getOrInsertFunction("printf", printfType);
  return printfCallee;
}

bool LabPass::doInitialization(Module &M) {
  return true;
}

bool LabPass::runOnModule(Module &M) {
  errs() << "runOnModule\n";

  LLVMContext &ctx = M.getContext();
  FunctionCallee printfCallee = printfPrototype(M);

  GlobalVariable * gvLevel = new GlobalVariable(M, IntegerType::getInt32Ty(ctx), false,
    GlobalValue::CommonLinkage, 0, "level");

  ConstantInt * cLevel0 = ConstantInt::get(IntegerType::getInt32Ty(ctx), 0);
  gvLevel->setInitializer(cLevel0);

  GlobalVariable * gvLoop = new GlobalVariable(M, IntegerType::getInt32Ty(ctx), false,
    GlobalValue::CommonLinkage, 0, "loop");

  ConstantInt * cLoop0 = ConstantInt::get(IntegerType::getInt32Ty(ctx), 0);
  gvLoop->setInitializer(cLoop0);

  for (auto &F : M) {
    if (F.empty()) {
      continue;
    }
    errs() << F.getName() << "\n";

    BasicBlock &Bstart = F.front();
    BasicBlock * Binfo = Bstart.splitBasicBlock(&Bstart.front(), "info");

    if (F.getName() != "main") {
      IRBuilder<> BuilderStart(&Bstart.front());

      Value * vLevel = BuilderStart.CreateLoad(Type::getInt32Ty(ctx), gvLevel);
      Value * aLevel = BuilderStart.CreateAdd(BuilderStart.getInt32(1), vLevel);
      BuilderStart.CreateStore(aLevel, gvLevel);
      BuilderStart.CreateStore(aLevel, gvLoop);

      BasicBlock * Bident = BasicBlock::Create(ctx, "ident", &F, Binfo);
      IRBuilder<> BuilderIdent(Bident);

      Instruction &br = Bstart.back();
      IRBuilder<> BuilderBr(&br);

      BuilderBr.CreateBr(Bident);
      br.eraseFromParent();

      BuilderIdent.CreateCall(printfCallee, { getI8StrVal(M, " ", "ident_space") });
      Value * vLoop = BuilderIdent.CreateLoad(Type::getInt32Ty(ctx), gvLoop);
      Value * aLoop = BuilderIdent.CreateSub(vLoop, BuilderIdent.getInt32(1));
      BuilderIdent.CreateStore(aLoop, gvLoop);
      Value * eq = BuilderIdent.CreateICmpEQ(aLoop, BuilderIdent.getInt32(0));
      BuilderIdent.CreateCondBr(eq, Binfo, Bident);
    }

    IRBuilder<> BuilderInfo(&Binfo->front());

    Constant * cFFmt = getI8StrVal(M, "%s: %014p\n", "f_fmt_" + F.getName());
    Constant * cFName = getI8StrVal(M, F.getName().str().c_str(), "f_name_" + F.getName());

    Constant * fAddr = ConstantExpr::getBitCast(&F, Type::getInt8PtrTy(ctx));
    BuilderInfo.CreateCall(printfCallee, { cFFmt, cFName, fAddr });

    BasicBlock &Bend = F.back();
    BasicBlock * Bret = Bend.splitBasicBlock(&Bend.back(), "ret");
    IRBuilder<> BuilderRet(&Bret->front());

    Value * vLevel = BuilderRet.CreateLoad(Type::getInt32Ty(ctx), gvLevel);
    Value * aLevel = BuilderRet.CreateSub(vLevel, BuilderRet.getInt32(1));
    BuilderRet.CreateStore(aLevel, gvLevel);
  }

  return true;
}

static RegisterPass<LabPass> X("labpass", "Lab Pass", false, false);