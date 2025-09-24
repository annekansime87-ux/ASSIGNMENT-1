import array

# Integers: Volunteer hours logged by individuals
volunteer_hours = [5, 8, 12, 7, 10, 6, 9]
total_hours = sum(volunteer_hours)
average_hours = total_hours / len(volunteer_hours)
min_hours = min(volunteer_hours)
max_hours = max(volunteer_hours)

# Strings: Formatted report using f-strings
report = (
    f"Total Volunteer Hours: {total_hours}\n"
    f"Average Volunteer Hours: {average_hours:.2f}\n"
    f"Minimum Hours: {min_hours}, Maximum Hours: {max_hours}"
)
print("Volunteer Hours Report:")
print(report)

# Booleans: Apply threshold condition
threshold = 8
if average_hours > threshold and max_hours > 10:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# Lists: Modify and display list
print("\nOriginal Hours List:", volunteer_hours)
volunteer_hours.append(11)  # Add new record
volunteer_hours = [h for h in volunteer_hours if h >= 6]  # Remove hours < 6
volunteer_hours.sort()
print("Modified and Sorted Hours List:", volunteer_hours)

# Arrays: Store subset and compare sums
hours_array = array.array('i', volunteer_hours[:5])  # Fixed-size subset
array_sum = sum(hours_array)
list_sum = sum(volunteer_hours[:5])
print(f"\nSum of array subset: {array_sum}")
print(f"Sum of list subset: {list_sum}")
print("Array and list sums match:", array_sum == list_sum)

# Dictionaries: List of volunteer records
volunteer_log = [
    {'id': 1, 'name': 'Alice', 'value': 5},
    {'id': 2, 'name': 'Bob', 'value': 8},
    {'id': 3, 'name': 'Charlie', 'value': 12},
    {'id': 4, 'name': 'Diana', 'value': 7}
]

# Update Charlie's hours
for record in volunteer_log:
    if record['name'] == 'Charlie':
        record['value'] = 14

# Delete Bob's record
volunteer_log = [record for record in volunteer_log if record['name'] != 'Bob']

# Compute total value
total_logged = sum(record['value'] for record in volunteer_log)
print("\nUpdated Volunteer Log:")
for record in volunteer_log:
    print(record)
print(f"Total Logged Hours from Records: {total_logged}")