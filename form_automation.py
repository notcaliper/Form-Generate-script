import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import concurrent.futures

# List of random first and last names
first_names = [
    "Jayesh", "Savya", "Ajay", "Ankit", "Sujit", "Aditya", "Swanandi", "Sakshi", 
    "Tejas", "Yash", "Baswadeep", "Omraj", "Shivam", "Prajakta", "Pratap", "Manish", 
    "Rohit", "Rushikesh", "Kunal", "Pallav", "Virat", "Arihant", "Siddhant", "Sachin", 
    "Dhurvesh", "Sushant", "Tanay", "Mayuresh", "Shivvardhan", "Shreyas", "Gaurav", 
    "Lakshit", "Parth", "Tanishq", "Sayandeep", "Prajwal", "Tanishk", "Bhupendra", 
    "SATWIK", "Ujjwal", "Yash", "Sarthu", "Jeet", "Hritik", "Sharad", "Dhruv", 
    "Tanmay", "Vaidehi", "Tanushk", "Raunak", "Rohan", "Tanishka", "Tavakkal", 
    "Pratham", "Aatish", "Jay", "Manasvi", "Kritika", "Ronit", "Ayush", "Shivansh", 
    "Shruti", "Yug", "Samarth", "Jyotiraditya", "Sakshat", "Pravin", "Parnil", 
    "Aryan", "Pragati", "Ishaan", "Abhiram", "Shubham", "Kaustubh", "Gargi", 
    "Prashant", "Bani", "Vishal", "Nitish", "Manas", "Vedant", "Lubdha", "Anirudh", 
    "Rohak", "Sanika", "Krishna", "Anushka", "Atharv", "Sanskar", "Priya", "Nitin"
]

last_names = [
    "Bhamare", "Bhalekar", "Vadnere", "Hire", "Deahmukh", "Bhende", "Choudhari", 
    "Bhandari", "Kanade", "Bendale", "Bembare", "Talekar", "Bhadane", "Mahale", 
    "Bhanapure", "Patil", "Dangat", "Suryawanshi", "Deshmukh", "Belkhede", "Bari", 
    "Bargir", "Vyavahare", "Dhamane", "Sarwade", "Barekar", "Wankhade", "Sonawane", 
    "Mitra", "Bavdhane", "Birari", "Jogi", "WABLE", "Saindanvise", "Waghmare", 
    "Jadhav", "Battawar", "Jachak", "Sonekar", "Sheikh", "Bhagat", "Bagal", 
    "Lonarkar", "Bhartiya", "Mukdam", "Dahiwal", "Pandey", "Bedage", "Ramawat", 
    "Kakde", "Shelke", "Bhosale", "Singh", "More", "Belokar", "Bandagar", "Dhondge", 
    "Nair", "Mailapure", "Padate", "Mathwale", "Borkar", "Netankar", "Barve", 
    "Mane", "Bhutada", "Kumar", "Chaudhari", "Sonkamble", "Auti"
]

# Age groups available in the form
age_groups = ["0 - 18", "18 - 29", "29 - 45", "45 or Above"]

# Fuel type options
fuel_types = [
    "Diesel - Power over everything! 🔥",
    "Petrol - I like the classics! ⛽",
    "CNG - Saving money AND the planet! 🌍 💰",
    "Hybrid/Electric - The future is here! ⚡ 🔋"
]

# Car preference options
car_preferences = [
    "Brand matters—Luxury speaks! 😎",
    "Give me a comfy ride, I don't care about the brand!",
    "Both! I want luxury AND comfort!",
    "Who cares? If it has four wheels and moves, I'm good. 🚗 💨"
]

# Transmission options
transmission_options = [
    "Manual - I like to feel in control! 🏁",
    "Automatic - My hands are busy holding coffee ☕",
    "Whatever gets me from point A to B!"
]

# Dream car options
dream_car_options = [
    "Sedan - Sleek and classy 😎",
    "SUV - I own the road! 🚙",
    "Hatchback - Compact but mighty! 🚗",
    "Convertible - Let the wind mess up my hair! 🌊 😍",
    "Truck - Because why not? 🚚"
]

# Budget options
budget_options = [
    "Whatever my wallet allows (Below ₹5,00,000)",
    "Reasonable but stylish (₹900000 - ₹1500000)",
    "Luxury on a budget (₹1600000 - ₹3000000)",
    "I want to feel like a millionaire (Above ₹30000000)"
]

# Sunroof options
sunroof_options = [
    "Yes! I love feeling like I'm in a music video 🎵 ☀️",
    "Nah, I don't want the sun frying my head ☀️ 🥵",
    "Only if it comes for free! 🤑"
]

# Safety feature options
safety_options = [
    "Super important! I want to survive the apocalypse! 💥",
    "As long as it has seatbelts, I'm good! 😂",
    "Safety? I drive like a pro! 🚗 💨"
]

# Advanced safety features options
advanced_safety_options = [
    "Yes! Safety first! 🚨",
    "Maybe, if it's not too expensive 💰",
    "Nah, I trust my own skills! 😏"
]

# Seating capacity options
seating_options = [
    "Two - Just me and my playlist 🎵",
    "Five - The usual squad setup 🚗",
    "Seven - Road trips need space! 🧳",
    "The more, the merrier! Bring the whole fam! 🥳"
]

# Driving frequency options
driving_frequency_options = [
    "Every day! My car is my second home 🏠",
    "A few times a week – depends on my mood 😎",
    "Only on weekends – My car needs rest too! 😂",
    "Rarely – My car feels abandoned! 😔"
]

# New vs used car options
new_used_options = [
    "New! Nothing beats that fresh car smell! 🚗 ✨",
    "Used - It's already broken in! 😎",
    "Depends on the deal I get! 🔍"
]

# Self-driving car options
self_driving_options = [
    "Yes! I'd love to nap while driving! 💤",
    "Nope, I don't trust robots! 🤖",
    "Maybe... If they don't crash like my computer 🖥️"
]

def fill_google_form(form_url, entry_number=None):
    # Set up Chrome options with performance improvements
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")  # Disable extensions for faster loading
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-infobars")  # Disable infobars
    chrome_options.add_argument("--disable-notifications")  # Disable notifications
    chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking
    
    # Uncomment the line below if you want to run in headless mode (no browser UI)
    # chrome_options.add_argument("--headless")
    
    # Set up the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.set_page_load_timeout(30)  # Set page load timeout
    
    # Set a smaller window size to reduce rendering overhead but keep it visible
    driver.set_window_size(1024, 768)
    
    # For identification in logs
    entry_id = f"Entry {entry_number}: " if entry_number is not None else ""
    
    try:
        # Navigate to the form
        driver.get(form_url)
        
        # Wait for the form to load
        wait = WebDriverWait(driver, 10)  # Reduced wait time
        
        # ---- First Page ----
        print(f"{entry_id}Filling first page...")
        
        # Generate a random name
        random_first_name = random.choice(first_names)
        random_last_name = random.choice(last_names)
        full_name = f"{random_first_name} {random_last_name}"
        
        # Fill in the name field - faster method
        name_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']")))
        name_field.send_keys(full_name)
        
        # Select a random age group
        random_age_group = random.choice(age_groups)
        age_group_index = age_groups.index(random_age_group)
        
        # Find the age radio group and click directly
        radio_groups = driver.find_elements(By.CSS_SELECTOR, "div[role='radiogroup']")
        if radio_groups:
            age_radios = radio_groups[0].find_elements(By.CSS_SELECTOR, "div[role='radio']")
            if 0 <= age_group_index < len(age_radios):
                driver.execute_script("arguments[0].click();", age_radios[age_group_index])
        
        # Click the "Next" button to go to page 2 - using JavaScript for faster execution
        next_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Next']/..")))
        driver.execute_script("arguments[0].click();", next_button)
        
        # ---- Second Page (all the remaining questions) ----
        # Wait less time for the second page - it's usually faster to load
        time.sleep(1) 
        
        # Get all radio groups on the current page
        radio_groups = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='radiogroup']")))
        
        # Process all questions faster
        option_arrays = [
            fuel_types, car_preferences, transmission_options, dream_car_options,
            budget_options, sunroof_options, safety_options, advanced_safety_options,
            seating_options, driving_frequency_options, new_used_options, self_driving_options
        ]
        
        # For each radio group (question) on the page
        for i, group in enumerate(radio_groups):
            # Only scroll every few questions to reduce scrolling operations
            if i % 3 == 0:
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", group)
                time.sleep(0.1)  # Minimal pause after scrolling
            
            # Get the options for this question and choose one
            if i < len(option_arrays):
                options = option_arrays[i]
                random_option = random.randint(0, len(options)-1)
                
                # Get radio buttons for this question
                question_radios = group.find_elements(By.CSS_SELECTOR, "div[role='radio']")
                
                # Click using JavaScript for speed
                if random_option < len(question_radios):
                    driver.execute_script("arguments[0].click();", question_radios[random_option])
        
        # Submit the form - using JavaScript for faster execution
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)
        
        submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Submit']/..")))
        driver.execute_script("arguments[0].click();", submit_button)
        
        # Wait briefly for submission confirmation
        time.sleep(1)
        
        return f"{entry_id}Form submitted successfully for {full_name}"
        
    except Exception as e:
        return f"{entry_id}Error: {str(e)}"
    
    finally:
        # Close the browser
        driver.quit()

def run_multiple_submissions_parallel(form_url, num_entries, max_workers=3):
    """Run multiple form submissions in parallel to speed up the process."""
    print(f"Starting to fill {num_entries} entries using {max_workers} parallel workers...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tasks and store futures
        futures = [executor.submit(fill_google_form, form_url, i+1) for i in range(num_entries)]
        
        # Process results as they complete
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                print(result)
            except Exception as exc:
                print(f"Generated an exception: {exc}")
    
    print(f"\nCompleted all {num_entries} form submissions!")

# Use the actual Google Form URL
form_url = 'https://forms.gle/XXXXXXXXXX'

if __name__ == "__main__":
    try:
        # Ask user for number of entries to fill
        while True:
            try:
                num_entries = int(input("How many entries would you like to submit to the form? "))
                if num_entries <= 0:
                    print("Please enter a positive number.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
        
        # Ask for parallel execution settings
        parallel = input("Run submissions in parallel for faster execution? (y/n): ").lower()
        
        if parallel in ('y', 'yes'):
            # Determine how many parallel workers to use
            max_workers = 3  # Default
            try:
                worker_input = input(f"How many parallel browsers to run? (1-5, default={max_workers}): ")
                if worker_input.strip():
                    max_workers = max(1, min(5, int(worker_input)))
            except ValueError:
                print(f"Using default value of {max_workers} workers.")
            
            # Confirm with user
            print(f"You've chosen to submit {num_entries} entries using {max_workers} parallel browsers.")
            confirm = input("Proceed? (y/n): ").lower()
            
            if confirm in ('y', 'yes'):
                run_multiple_submissions_parallel(form_url, num_entries, max_workers)
            else:
                print("Operation cancelled by user.")
        else:
            # Confirm with user for sequential execution
            print(f"You've chosen to submit {num_entries} entries sequentially.")
            confirm = input("Proceed? (y/n): ").lower()
            
            if confirm in ('y', 'yes'):
                print("Running submissions one by one...")
                for i in range(num_entries):
                    print(f"\n--- Entry {i+1} of {num_entries} ---")
                    result = fill_google_form(form_url)
                    print(result)
                    
                    if i < num_entries - 1:
                        # Shorter wait between submissions
                        wait_time = random.uniform(0.5, 1.5)
                        print(f"Waiting {wait_time:.1f} seconds before next submission...")
                        time.sleep(wait_time)
                
                print(f"\nCompleted all {num_entries} form submissions!")
            else:
                print("Operation cancelled by user.")
            
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 
