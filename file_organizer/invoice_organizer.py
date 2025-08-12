import os

os.chdir('..\\file_organizer\\invoices')


def get_invoice_month_string(name):
    filename = name.split('.')[0]
    month = filename.split('_')[-1]
    return month


def move_file(filename, folder):
    os.rename(filename, os.path.join(folder, filename))


def main():
    for file in os.listdir():
        if get_invoice_month_string(file) is None:
            continue
        else:
            invoice_month = get_invoice_month_string(file)

        if invoice_month in os.listdir():
            if invoice_month == file:
                continue
            move_file(file, invoice_month)
        else:
            os.mkdir(invoice_month)
            move_file(file, invoice_month)


if __name__ == '__main__':
    main()
