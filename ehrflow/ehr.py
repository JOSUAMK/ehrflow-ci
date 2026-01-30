from dataclasses import dataclass

@dataclass
class PatientRecord:
    patient_id: str
    diagnosis: str
    treatment: str

def validate_record(record: PatientRecord) -> bool:
    return all([
        isinstance(record.patient_id, str) and record.patient_id,
        isinstance(record.diagnosis, str) and record.diagnosis,
        isinstance(record.treatment, str) and record.treatment,
    ])
