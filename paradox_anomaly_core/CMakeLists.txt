set(SRC_FILES 
    src/paradox_anomaly_core.cpp
    src/paradox_anomaly_tenant.cpp
)

add_library(paradox_anomaly_core ${SRC_FILES})

set_property(TARGET paradox_anomaly_core PROPERTY CXX_STANDARD 23)

target_include_directories(paradox_anomaly_core PUBLIC include)
