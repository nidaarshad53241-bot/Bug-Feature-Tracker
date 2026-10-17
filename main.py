# === Bug & Feature Tracker ===

entries = []

def add_entry():
    title = input("Enter title: ").strip()
    if not title:
        print("Error: Title cannot be empty!")
        return
    desc = input("Enter description: ")
    type_ = input("Enter type (Bug/Feature): ")
    entries.append({"title": title, "desc": desc, "type": type_})
    print("Entry added!")

def view_entries():
    if not entries:
        print("No entries found.")
        return
    for i, e in enumerate(entries, 1):
        print(f"{i}. {e['title']} - {e['type']}")

def show_statistics():
    bugs = sum(1 for e in entries if e['type'].lower() == 'bug')
    features = len(entries) - bugs
    print(f"Total: {len(entries)}, Bugs: {bugs}, Features: {features}")

def main():
    while True:
        print("\n=== Bug & Feature Tracker ===")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Show Statistics")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            show_statistics()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again. (Validation works!)")

if __name__ == "__main__":
    main()