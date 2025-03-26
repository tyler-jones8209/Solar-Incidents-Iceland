import csv

# A function that calculates the average sunshine between either April to August or September to March
# I chose these sections because the amount of sun seemed to drastically dip between August and September and drastically increase between March and April
def calculate_seasonal_sunshine(rows):
    light_months = {4, 5, 6, 7, 8}  # April to August
    dark_months = {9, 10, 11, 12, 1, 2, 3}  # September to March

    light_total, light_count = 0, 0
    dark_total, dark_count = 0, 0

    for row in rows:
        month = int(row[2])
        sun = float(row[16].strip())

        if month in light_months:
            light_total += sun
            light_count += 1
        elif month in dark_months:
            dark_total += sun
            dark_count += 1

    light_avg = round(light_total / light_count) if light_count > 0 else 0
    dark_avg = round(dark_total / dark_count) if dark_count > 0 else 0

    return light_avg, dark_avg

# A function that lets you specify the range in years you want to calculate
def calculate_year_range(rows, years):
    if not rows:
        return []
    last_year = int(rows[-1][1])
    start_year = max(last_year - years, int(rows[0][1]))

    filtered_rows = []
    for row in rows:
        year = int(row[1])
        if start_year <= year <= last_year:
            filtered_rows.append(row)

    return filtered_rows, start_year, last_year

# The function that actually opens and takes data from the CSV files
def open_csv(input_file):
    with open(input_file, 'r') as file:
        data = csv.reader(file)
        next(data)  # Skip the header row
        next(data)  # Skip the second row

        # Collect valid rows, determined on if the 'sun' value is NA or not
        all_valid_rows = []
        for row in data:
            sun = row[16].strip()
            if sun.lower() == "na" or sun == "":  # Skip invalid rows
                continue
            sun = float(sun)
            all_valid_rows.append(row)

        # Store the first valid year for the unfiltered year range
        first_year = int(all_valid_rows[0][1])

        # Calculate the year range I want to use. In this case, it's 30 years
        thirty_year_rows, thirty_start_year, last_year = calculate_year_range(all_valid_rows, 30)

        # Calculate total sunshine average for unfiltered year range
        sun_total = sum(float(row[16]) for row in all_valid_rows)
        count_total = len(all_valid_rows)
        sun_total_avg = round(sun_total / count_total) if count_total > 0 else 0

        # Calculate total sunshine for the last 30 years
        thirty_sun_total = sum(float(row[16]) for row in thirty_year_rows)
        thirty_count = len(thirty_year_rows)
        thirty_sun_avg = round(thirty_sun_total / thirty_count) if thirty_count > 0 else 0

        # Calculate seasonal averages for all the years
        total_light_avg, total_dark_avg = calculate_seasonal_sunshine(all_valid_rows)
        
        # Calculate seasonal averages for the 30 years
        thirty_light_avg, thirty_dark_avg = calculate_seasonal_sunshine(thirty_year_rows)

        # Extract the name of the station from the input file
        location = input_file.split("/")[1].split("_")[0].upper()

        # Print stats for storing in seperate file. Too lazy to create seperate function for that
        print(f"Showing stats for: {location} STATION")
        
        print("----------TOTAL STATS----------")
        print(f"Average sunshine from {first_year} to {last_year}: {round(sun_total_avg)} hours per month.")
        print(f"April to August average: {total_light_avg} hours/month")
        print(f"September to March average: {total_dark_avg} hours/month")

        print("----------30 YEAR STATS----------")
        print(f"Average sunshine from {thirty_start_year} to {last_year}: {round(thirty_sun_avg)} hours per month.")
        print(f"April to August average: {thirty_light_avg} hours/month")
        print(f"September to March average: {thirty_dark_avg} hours/month")

        


open_csv('station_data/Akureyri_data.csv')
