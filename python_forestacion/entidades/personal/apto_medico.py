from datetime import date

class AptoMedico:
    """
    Representa el certificado de aptitud médica de un trabajador.
    """
    def __init__(self, fecha_emision: date, fecha_vencimiento: date, es_apto: bool):
        """
        Inicializa el apto médico.

        Args:
            fecha_emision: Fecha de emisión del certificado.
            fecha_vencimiento: Fecha de vencimiento del certificado.
            es_apto: True si el trabajador está apto.
        """
        if fecha_vencimiento < fecha_emision:
            raise ValueError("La fecha de vencimiento no puede ser anterior a la de emisión.")

        self._fecha_emision = fecha_emision
        self._fecha_vencimiento = fecha_vencimiento
        self._es_apto = es_apto

    def get_fecha_emision(self) -> date:
        return self._fecha_emision

    def get_fecha_vencimiento(self) -> date:
        return self._fecha_vencimiento

    def es_apto(self) -> bool:
        return self._es_apto

    def esta_vencido(self, fecha_actual: date) -> bool:
        """Verifica si el apto médico está vencido en la fecha actual."""
        return fecha_actual > self._fecha_vencimiento
