// JUnit 5 tests for Thermostat.java
// Satisfy CACC (correlated active clause coverage)

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;
import java.util.*;

public class ThermostatCACCTest
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
        // set 4 clauses to false by default
        thermostat.setCurrentTemp(0);
        thermostat.setThresholdDiff(65);
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

    // UPPERCASE: major
    // lowercase: minor
    // underscore: predicate result

    @Test
    public void Ffft_F()
    {
        // minor
        setC4True();
        // assert
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, false, "major: c1/F, predicate: F");
    }

    @Test
    public void Tfft_T()
    {
        // major
        setC1True();
        // minor
        setC4True();
        // assert
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, true, "major: c1/T, predicate: T");
    }

    @Test
    public void fFtt_F()
    {
        // minor
        setC3True();
        setC4True();
        // assert
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, false, "major: c2/F, predicate: F");
    }

    @Test
    public void fTtt_T()
    {
        // major
        setC2True();
        // minor
        setC3True();
        setC4True();
        // assert
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, true, "major: c2/T, predicate: T");
    }

    @Test
    public void ftFt_F()
    {
        // minor
        setC2True();
        setC4True();
        // assert
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, false, "major: c3/F, predicate: F");
    }

    @Test
    public void ftTt_T()
    {
        // major
        setC3True();
        // minor
        setC2True();
        setC4True();
        // assert
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, true, "major: c3/T, predicate: T");
    }

    @Test
    public void tffF_F()
    {
        // minor
        setC1True();
        // assert
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, false, "major: c4/F, predicate: F");
    }

    @Test
    public void tffT_T()
    {
        setC4True();
        // minor
        setC1True();
        // assert
        boolean heaterOn = thermostat.turnHeaterOn(pSet);
        assertEquals(heaterOn, true, "major: c4/T, predicate: T");
    }

    void setC1True()
    {
        thermostat.setThresholdDiff(0);
    }

    void setC2True()
    {
        thermostat.setOverride(true);
    }

    void setC3True()
    {
        thermostat.setOverTemp(66);
    }

    void setC4True()
    {
        thermostat.setTimeSinceLastRun(1);
    }

    void doNothing()
    {
        do {} while (false);
    }
}
