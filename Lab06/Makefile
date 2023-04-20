PROGS := hoob soob goob uaf uar readzone

ASANFG := -fsanitize=address -fno-omit-frame-pointer
CFLAGS := -O1 -g -w
BINFLD := valg asan

all: $(PROGS)

$(PROGS): %: src/%.c $(BINFLD)
	gcc $(CFLAGS) $< -o valg/$@
	gcc $(CFLAGS) $(ASANFG) $< -o asan/$@

$(BINFLD):
	mkdir $@

clean:
	rm -rf $(BINFLD)
