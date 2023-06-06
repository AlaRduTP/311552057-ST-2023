// JUnit 5 tests for Thermostat.java
// Satisfy CC (clause coverage)

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;
import java.util.*;

public class ThermostatCCTest
{
    private static final ProgrammedSettings pSet = new ProgrammedSettings();
    private static final DayType CUR_DAY = DayType.WEEKDAY;
    private static final Period CUR_PERIOD = Period.MORNING;
    private static Thermostat thermostat = new Thermostat();

    @BeforeAll
    public static void initPSet()
    {
        thermostat.setDay(CUR_DAY);
        thermostat.setPeriod(CUR_PERIOD);
    }

    @BeforeEach
    public void initThermostat()
    {
        thermostat.setCurrentTemp(0);
        thermostat.setThresholdDiff(0);
        thermostat.setTimeSinceLastRun(0);
        thermostat.setMinLag(0);
        thermostat.setOverride(false);
        thermostat.setOverTemp(0);
    }

    // 4 clauses:
    //   curTemp < dTemp - thresholdDiff
    //   override
    //   curTemp < overTemp - thresholdDiff
    //   timeSinceLastRun > minLag

    @Test
    public void cFFFF()
    {
        thermostat.setThresholdDiff(65);
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, false, "clauses: F, F, F, F");
    }

    @Test
    public void cTTTT()
    {
        thermostat.setOverride(true);
        thermostat.setOverTemp(1);
        thermostat.setTimeSinceLastRun(1);
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, true, "clauses: T, T, T, T");
    }
}
