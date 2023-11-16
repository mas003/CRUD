import csv
import os

csv_filename = 'students.csv'
fieldnames = ['NIM', 'Nama', 'Jurusan']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("=== APLIKASI MAHASISWA ===")
    print("[1] Lihat Daftar Mahasiswa")
    print("[2] Tambah Mahasiswa Baru")
    print("[3] Edit Data Mahasiswa")
    print("[4] Hapus Data Mahasiswa")
    print("[0] Keluar")
    print("------------------------")
    selected_menu = input("Pilih menu> ")
    
    if selected_menu == "1":
        show_students()
    elif selected_menu == "2":
        add_student()
    elif selected_menu == "3":
        edit_student()
    elif selected_menu == "4":
        delete_student()
    elif selected_menu == "0":
        exit()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

def read_students():
    students = []
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                students.append(row)
    except FileNotFoundError:
        pass
    return students

def write_students(students):
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def show_students():
    clear_screen()
    students = read_students()

    if len(students) > 0:
        print(f"{fieldnames[0]} \t {fieldnames[1]} \t\t {fieldnames[2]}")
        print("-" * 34)
        for data in students:
            print(f"{data['NIM']} \t {data['Nama']} \t {data['Jurusan']}")
    else:
        print("Tidak ada data mahasiswa!")

    back_to_menu()

def show_students_for_edit_delete():
    clear_screen()
    students = read_students()

    if len(students) > 0:
        print(f"{fieldnames[0]} \t {fieldnames[1]} \t\t {fieldnames[2]}")
        print("-" * 34)
        for data in students:
            print(f"{data['NIM']} \t {data['Nama']} \t {data['Jurusan']}")
    else:
        print("Tidak ada data mahasiswa!")

def add_student():
    clear_screen()
    students = read_students()

    nim = input("NIM: ")
    nama = input("Nama: ")
    jurusan = input("Jurusan: ")

    students.append({'NIM': nim, 'Nama': nama, 'Jurusan': jurusan})
    write_students(students)

    print("Data mahasiswa berhasil disimpan!")
    back_to_menu()

def edit_student():
    clear_screen()
    students = read_students()
    show_students_for_edit_delete()

    nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
    found_student = next((student for student in students if student['NIM'] == nim), None)

    if found_student:
        new_nama = input("Nama baru: ")
        new_jurusan = input("Jurusan baru: ")

        found_student['Nama'] = new_nama
        found_student['Jurusan'] = new_jurusan

        write_students(students)  # Menuliskan kembali seluruh daftar mahasiswa
        print("Data mahasiswa berhasil diubah!")
    else:
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

    back_to_menu()

def delete_student():
    clear_screen()
    students = read_students()
    show_students_for_edit_delete()

    nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
    students = [student for student in students if student['NIM'] != nim]

    write_students(students)  # Menuliskan kembali daftar mahasiswa setelah penghapusan
    print("Data mahasiswa berhasil dihapus!")

    back_to_menu()


if __name__ == "__main__":
    while True:
        show_menu()
