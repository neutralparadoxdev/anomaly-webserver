set(MAIN_FILE src/main.cpp)

add_executable(paradox_anomaly_server ${MAIN_FILE})

set_property(TARGET paradox_anomaly_server PROPERTY CXX_STANDARD 23)

target_link_libraries(paradox_anomaly_server PRIVATE paradox_anomaly_core)
