class HealthDataSystem:
    def __init__(self):
        self.records = []

    def add_record(self, name, age, gender, condition):
        record = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Condition": condition
        }
        self.records.append(record)
        print(f"Record for {name} added successfully.")

    def view_records(self):
        if not self.records:
            print("No records available.")
        else:
            print("\nHealth Records:")
            for i, record in enumerate(self.records, start=1):
                print(f"Record {i}:")
                for key, value in record.items():
                    print(f"  {key}: {value}")

    def search_record(self, name):
        found = [record for record in self.records if record["Name"].lower() == name.lower()]
        if not found:
            print(f"No records found for {name}.")
        else:
            print(f"\nRecords found for {name}:")
            for record in found:
                for key, value in record.items():
                    print(f"  {key}: {value}")

    def delete_record(self, name):
        initial_count = len(self.records)
        self.records = [record for record in self.records if record["Name"].lower() != name.lower()]
        if len(self.records) < initial_count:
            print(f"Record(s) for {name} deleted successfully.")
        else:
            print(f"No records found for {name} to delete.")

# Example Usage
if __name__ == "__main__":
    system = HealthDataSystem()

    # Adding records
    system.add_record("Alice", 30, "Female", "Diabetes")
    system.add_record("Bob", 45, "Male", "Hypertension")

    # Viewing records
    system.view_records()

    # Searching for a specific record
    system.search_record("Alice")

    # Deleting a record
    system.delete_record("Bob")

    # Viewing records again
    system.view_records()
