from collections import namedtuple


class MedicalRecord:

    @staticmethod
    def merge(*records):
        """
        :param records: (varargs list of namedtuple) The patient details.
        :returns: (namedtuple) named Patient, containing details from all records, in entry order.
        """
        field_names_to_values = {}
        for record in records:
            for field_name in record._fields:
                field_names_to_values[field_name] = getattr(record, field_name)

        Patient = namedtuple('Patient', field_names_to_values.keys())

        return Patient(**field_names_to_values)


PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth'])
personal_details = PersonalDetails(date_of_birth='06-04-1972')

Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color='Blue', hair_color='Black')

print(MedicalRecord.merge(personal_details, complexion))
