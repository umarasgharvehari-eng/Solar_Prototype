def calculate_load(appliances):
    total_kwh = 0
    total_watts = 0

    for a in appliances:
        watts = a["watts"]
        qty = a["qty"]
        hours = a["hours"]

        total_watts += watts * qty
        total_kwh += (watts * qty * hours) / 1000

    return total_kwh, total_watts


def solar_size(daily_kwh):
    sun_hours = 5
    efficiency = 0.75
    return daily_kwh / (sun_hours * efficiency)


def battery_size(load_watts, backup_hours):
    return (load_watts * backup_hours) / 1000


def system_cost(solar_kw, battery_kwh):
    panel_cost = solar_kw * 1000 * 35
    battery_cost = battery_kwh * 50000
    inverter_cost = 200000

    return panel_cost + battery_cost + inverter_cost
