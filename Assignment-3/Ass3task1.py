# TGNPDCL Billing Application (simple, configurable)

from typing import Dict, Union, List, Tuple

DEFAULT_TARIFFS = {
    'domestic':    {'fixed_charge': 50.0,  'customer_charge': 30.0},
    'commercial':   {'fixed_charge': 150.0, 'customer_charge': 100.0},
    'industrial':   {'fixed_charge': 250.0, 'customer_charge': 150.0},
    'agriculture':  {'fixed_charge': 20.0,  'customer_charge': 10.0},
}

def calculate_tg_bill(units: float,
                      pu: float = None,
                      customer_type: str = 'domestic',
                      meter_rent: float = 0.0,
                      other_charges: float = 0.0,
                      ed_rate: float = 0.05,
                      tariffs: Dict[str, Dict[str, float]] = DEFAULT_TARIFFS
                      ) -> Dict[str, float]:
    """
    Calculate a simplified electricity bill.

    Basic model: EC = units * pu
    FC, CC from tariff table by customer_type
    ED = EC * ed_rate
    Total = EC + FC + CC + ED + meter_rent + other_charges

    Arguments:
      units: units consumed (kWh)
      pu: price per unit (Rs). Required unless you implement slab logic here.
      customer_type: 'domestic'|'commercial'|'industrial'|'agriculture'
      meter_rent, other_charges: additional fixed amounts
      ed_rate: electricity duty rate (fraction)
      tariffs: table with fixed and customer charges per type

    Returns:
      dict with keys: EC, FC, CC, ED, Other, Total
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")
    ct = customer_type.strip().lower()
    if ct not in tariffs:
        raise ValueError(f"Unknown customer type '{customer_type}'. Valid: {list(tariffs.keys())}")

    if pu is None:
        raise ValueError("PU (price per unit) must be provided in this simple model. To use slab rates, modify the function.")

    EC = float(units) * float(pu)
    FC = float(tariffs[ct]['fixed_charge'])
    CC = float(tariffs[ct]['customer_charge'])
    ED = EC * float(ed_rate)
    Other = float(meter_rent) + float(other_charges)
    Total = EC + FC + CC + ED + Other

    # Round amounts for display
    return {
        'EC': round(EC, 2),
        'FC': round(FC, 2),
        'CC': round(CC, 2),
        'ED': round(ED, 2),
        'Other': round(Other, 2),
        'Total': round(Total, 2)
    }

def prompt_and_print():
    """Interactive prompt to read inputs and print bill breakdown."""
    try:
        units = float(input("Enter units consumed (CU): ").strip())
        pu = float(input("Enter price per unit (PU) in Rs (e.g. 5.50): ").strip())
        ctype = input("Enter customer type (domestic/commercial/industrial/agriculture): ").strip()
        meter_rent = input("Enter meter rent (press Enter for 0): ").strip()
        other = input("Enter other charges (press Enter for 0): ").strip()
        ed = input("Enter electricity duty rate as percent (e.g. 5 for 5%, Enter for 5%): ").strip()

        meter_rent = float(meter_rent) if meter_rent else 0.0
        other = float(other) if other else 0.0
        ed_rate = float(ed)/100.0 if ed else 0.05

        bill = calculate_tg_bill(units, pu, ctype, meter_rent=meter_rent, other_charges=other, ed_rate=ed_rate)

        print("\n--- Electricity Bill ---")
        print(f"Input: Units={units}, PU=Rs {pu}, Type={ctype}")
        print(f"  EC (Energy Charges): Rs {bill['EC']}")
        print(f"  FC (Fixed Charges): Rs {bill['FC']}")
        print(f"  CC (Customer Charges): Rs {bill['CC']}")
        print(f"  ED (Electricity Duty): Rs {bill['ED']}")
        print(f"  Other Charges (meter rent + others): Rs {bill['Other']}")
        print(f"  Total Bill: Rs {bill['Total']}")
    except Exception as e:
        print("Error:", str(e))

if __name__ == '__main__':
    # Example runnable non-interactive test:
    example_bill = calculate_tg_bill(units=250, pu=5.50, customer_type='Domestic', meter_rent=20.0, other_charges=15.0, ed_rate=0.05)
    print("Example inputs: Units=250, PU=5.50, Type=Domestic, MeterRent=20, Other=15, ED=5%")
    for k,v in example_bill.items():
        print(f"{k}: Rs {v}")
    print("\nRun prompt_and_print() or run this file directly to enter your own values.")