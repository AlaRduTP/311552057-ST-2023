// JUnit 5 tests for Thermostat.java
// Satisfy PC (predicate coverage)

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;
import java.util.*;

public class ThermostatPCTest
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

    @Test
    public void pFalse()
    {
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, false, "predicate: false");
    }

    @Test
    public void pTrue()
    {
        thermostat.setTimeSinceLastRun(1);
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, true, "predicate: true");
    }
}
