#pragma once

#include <string>

namespace paradox_anomaly
{
namespace core
{
/**
 * A tenant 
 */
class Tenant
{
public:
    Tenant()=default;
    virtual ~Tenant();
private:
    std::string mHost;
};
}
}
