#pragma once

#include <memory>
#include <vector>
#include <thread>
#include <string>
#include <optional>

#include <paradox_anomaly_core/paradox_anomaly_listener.h>
#include <paradox_anomaly_core/paradox_anomaly_tenant.h>
#include <paradox_anomaly_core/paradox_anomaly_connection.h>

namespace paradox_anomaly
{
namespace core
{
/**
 * Paradox Anomaly Core
 *
 * This is the core part of the application.
 *
 */
class ParadoxAnomalyCore
{
public:
    ParadoxAnomalyCore(std::string ip, int port);
    virtual ~ParadoxAnomalyCore();


    /**
     * Add a tenant to the application
     */
    void AddTenant(std::unique_ptr<Tenant> tenant);

    /**
     * Start the server.
     * 
     * This call completes when the server is halted.
     */
    int Run();

private:
    /// tls listener
    std::optional<Listener> mTLS;

    /// plain text connection
    std::optional<Listener> mPlainText;

    /// active connections
    std::vector<std::unique_ptr<Connection>> mConnections;

    /// worker threads
    std::vector<std::thread> mWorkers;

    /// tenants
    std::vector<std::unique_ptr<Tenant>> mTenants;
};
}
}
