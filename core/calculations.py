import math

def calculate_load(appliances):
    total_daily_kwh = 0
    total_connected_watts = 0

    for a in appliances:
        watts = float(a.get("watts", 0))
        qty = int(a.get("qty", 0))
        hours = float(a.get("hours", 0))
        on_solar = a.get("on_solar", True)
        backup_required = a.get("backup_required", False)

        item_connected_watts = watts * qty
        item_daily_kwh = (watts * qty * hours) / 1000

        total_connected_watts += item_connected_watts

        if on_solar:
            total_daily_kwh += item_daily_kwh

    return total_daily_kwh, total_connected_watts


def calculate_backup_load(appliances):
    backup_watts = 0
    for a in appliances:
        if a.get("backup_required", False):
            backup_watts += float(a.get("watts", 0)) * int(a.get("qty", 0))
    return backup_watts


def solar_size_required(daily_kwh, sun_hours=5.0, performance_ratio=0.78):
    if sun_hours <= 0 or performance_ratio <= 0:
        return 0
    return daily_kwh / (sun_hours * performance_ratio)


def battery_size_required(backup_watts, backup_hours, dod=0.9, efficiency=0.9):
    if backup_hours <= 0 or backup_watts <= 0:
        return 0
    required_energy = (backup_watts * backup_hours) / 1000
    usable_factor = dod * efficiency
    if usable_factor <= 0:
        return 0
    return required_energy / usable_factor


def panel_count_required(solar_kw, panel_watt):
    if panel_watt <= 0:
        return 0
    total_required_watts = solar_kw * 1000
    return math.ceil(total_required_watts / panel_watt)


def actual_panel_capacity_kw(panel_count, panel_watt):
    return (panel_count * panel_watt) / 1000


def estimate_monthly_generation(actual_solar_kw, sun_hours=5.0, performance_ratio=0.78):
    return actual_solar_kw * sun_hours * 30 * performance_ratio


def estimate_monthly_savings(monthly_generation_kwh, import_tariff=65):
    return monthly_generation_kwh * import_tariff


def estimate_payback_years(total_cost, monthly_savings):
    if monthly_savings <= 0:
        return 0
    annual_savings = monthly_savings * 12
    return total_cost / annual_savings


def recommend_inverter_size(solar_kw):
    if solar_kw <= 3:
        return 3
    elif solar_kw <= 5:
        return 5
    elif solar_kw <= 6:
        return 6
    elif solar_kw <= 8:
        return 8
    elif solar_kw <= 10:
        return 10
    return round(solar_kw)


def calculate_system_cost(
    panel_count,
    panel_watt,
    panel_price_per_watt,
    battery_kwh,
    battery_price_per_kwh,
    inverter_price,
    installation_cost,
    structure_cost,
    bos_cost,
    transport_cost,
):
    panel_cost = panel_count * panel_watt * panel_price_per_watt
    battery_cost = battery_kwh * battery_price_per_kwh

    total_cost = (
        panel_cost
        + battery_cost
        + inverter_price
        + installation_cost
        + structure_cost
        + bos_cost
        + transport_cost
    )

    return {
        "panel_cost": panel_cost,
        "battery_cost": battery_cost,
        "inverter_cost": inverter_price,
        "installation_cost": installation_cost,
        "structure_cost": structure_cost,
        "bos_cost": bos_cost,
        "transport_cost": transport_cost,
        "total_cost": total_cost,
    }
