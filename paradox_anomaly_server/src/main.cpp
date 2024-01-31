#include <iostream>
#include <string>

#include <paradox_anomaly_core/paradox_anomaly_core.h>

int main(int argc, char** argv)
{
    paradox_anomaly::core::ParadoxAnomalyCore core("0.0.0.0", 4555);

    return core.Run();
}
