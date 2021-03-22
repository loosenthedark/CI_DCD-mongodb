import os
import pymongo
if os.path.exists('env.py'):
    import env


MONGO_URI = os.environ.get('MONGO_URI')
DATABASE = 'myFirstDB'
COLLECTION = 'celebrities'


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to MongoDB!!!: %s') % e


def show_menu():
    # Leave blank line at top of menu for readability/visual purposes
    print('')
    print('1. Add a record')
    print('2. Find a record by name')
    print('3. Edit a record')
    print('4. Delete a record')
    print('5. Exit menu')

    option = input('Select option: ')
    return option


# Reusable helper function
def get_record():
    # Blank line again left at top of menu for readability
    print('')
    first = input('Enter first name > ')
    last = input('Enter last name > ')

    # Search (by name) functionality
    try:
        doc = coll.find_one({"first": first.lower(), "last": last.lower()})
    except:
        # Blank line again left for visual purposes
        print('')
        print('Problem accessing the database!')

    if not doc:
        # Blank line again left for visual purposes
        print('')
        print('Error! No results found.')

    return doc


def add_record():
    # Blank line again left at top of menu for readability
    print('')
    first = input('Enter first name > ')
    last = input('Enter last name > ')
    dob = input('Enter date of birth > ')
    gender = input('Enter gender > ')
    hair_color = input('Enter hair color > ')
    occupation = input('Enter occupation > ')
    nationality = input('Enter nationality > ')

    new_doc = {
        "first": first.lower(),
        "last": last.lower(),
        "dob": dob,
        "gender": gender,
        "hair_color": hair_color,
        "occupation": occupation,
        "nationality": nationality
    }

    try:
        coll.insert(new_doc)
        # Blank line again left for visual purposes
        print('')
        print('Document successfully inserted!')
    except:
        # Blank line again left for visual purposes
        print('')
        print('Problem accessing the database!')


def find_record():
    doc = get_record()
    if doc:
        # Blank line again left for visual purposes
        print('')
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        # Blank line again left for visual purposes
        print('')
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + ' [' + v.capitalize() + '] > ')

                if update_doc[k] == '':
                    update_doc[k] = v

        try:
            coll.update_one(doc, {"$set": update_doc})
            # Blank line again left for visual purposes
            print('')
            print('Documented successfully updated!')
        except:
            # Blank line again left for visual purposes
            print('')
            print('Problem accessing the database!')


def delete_record():
    doc = get_record()
    if doc:
        # Blank line again left for visual purposes
        print('')
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        # Blank line again left for visual purposes
        print('')
        confirmation = input('Is this the record you want to delete?\nY / N > ')
         # Blank line again left for visual purposes
        print('')

        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                # Blank line again left for visual purposes
                print('')
                print('Documented successfully deleted!')
            except:
                # Blank line again left for visual purposes
                print('')
                print('Problem accessing the database!')            
        else:
            print('Document not deleted.')


def main_loop():
    while True:
        option = show_menu()
        if option == '1':
            add_record()
        elif option == '2':
            find_record()
        elif option == '3':
            edit_record()
        elif option == '4':
            delete_record()
        elif option == '5':
            conn.close()
            break
        else:
            print('Invalid option selected!')
        # Another blank line left here for visual purposes
        print('')
        
conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()