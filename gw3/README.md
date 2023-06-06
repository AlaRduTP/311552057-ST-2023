# Groupwork 3: Logic Coverage for Your Proposed Project

## Target

- `Themostat` class

## Dependencies

- JUnit 5
- gradle

## Run

```
$ gradle test
```

## Result

```
> Task :test

ThermostatCACCTest > Tfft_T() PASSED

ThermostatCACCTest > fFtt_F() PASSED

ThermostatCACCTest > fTtt_T() PASSED

ThermostatCACCTest > ftFt_F() PASSED

ThermostatCACCTest > ftTt_T() PASSED

ThermostatCACCTest > tffF_F() PASSED

ThermostatCACCTest > tffT_T() PASSED

ThermostatCACCTest > Ffft_F() PASSED

ThermostatCCTest > cFFFF() PASSED

ThermostatCCTest > cTTTT() PASSED

ThermostatPCTest > pFalse() PASSED

ThermostatPCTest > pTrue() PASSED

BUILD SUCCESSFUL in 1s
3 actionable tasks: 3 executed
```
