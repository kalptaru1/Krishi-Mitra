<<<<<<< HEAD
import requests

def get_crop_price(crop_type):
    """Fetch real-time crop prices using Google Search API (or an alternative API)."""
    # Dummy API endpoint (replace with actual)
    api_url = f"https://api.example.com/crop-prices?crop={crop_type}"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        return data.get("price_per_kg", 0)  # Default to 0 if not found
    except:
        return 0  # Fallback if API fails

def calculate_loan_amount(yield_amount, land_size, crop_type, years):
    base_loan = 10000  
    crop_factor = get_crop_price(crop_type)  # Get crop price from API
    if crop_factor == 0:  # If API fails, use defaults
        crop_factors = {"wheat": 800, "rice": 1000, "sugarcane": 1500, "cotton": 1200}
        crop_factor = crop_factors.get(crop_type.lower(), 500)

    loan_amount = base_loan + (yield_amount * crop_factor) + (land_size * 2000)

    interest_rates = {
        "Kisan Credit Card": 0.04,
        "PM Kisan Loan": 0.035,
        "General Agriculture Loan": 0.05
    }

    best_scheme = min(interest_rates, key=interest_rates.get)
    interest_rate = interest_rates[best_scheme]

    total_repayment = loan_amount + (loan_amount * interest_rate * years)

    return {
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "best_scheme": best_scheme,
        "total_repayment": total_repayment
    }
=======
import requests

def get_crop_price(crop_type):
    """Fetch real-time crop prices using Google Search API (or an alternative API)."""
    # Dummy API endpoint (replace with actual)
    api_url = f"https://api.example.com/crop-prices?crop={crop_type}"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        return data.get("price_per_kg", 0)  # Default to 0 if not found
    except:
        return 0  # Fallback if API fails

def calculate_loan_amount(yield_amount, land_size, crop_type, years):
    base_loan = 10000  
    crop_factor = get_crop_price(crop_type)  # Get crop price from API
    if crop_factor == 0:  # If API fails, use defaults
        crop_factors = {"wheat": 800, "rice": 1000, "sugarcane": 1500, "cotton": 1200}
        crop_factor = crop_factors.get(crop_type.lower(), 500)

    loan_amount = base_loan + (yield_amount * crop_factor) + (land_size * 2000)

    interest_rates = {
        "Kisan Credit Card": 0.04,
        "PM Kisan Loan": 0.035,
        "General Agriculture Loan": 0.05
    }

    best_scheme = min(interest_rates, key=interest_rates.get)
    interest_rate = interest_rates[best_scheme]

    total_repayment = loan_amount + (loan_amount * interest_rate * years)

    return {
        "loan_amount": loan_amount,
        "interest_rate": interest_rate,
        "best_scheme": best_scheme,
        "total_repayment": total_repayment
    }
>>>>>>> f8b7ddb (Initial commit)
