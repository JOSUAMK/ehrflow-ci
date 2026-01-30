from ehrflow.ehr import PatientRecord, validate_record

def test_valid_record():
    record = PatientRecord("P100", "Flu", "Rest")
    assert validate_record(record)

def test_invalid_record():
    record = PatientRecord("", "Flu", "Rest")
    assert not validate_record(record)
