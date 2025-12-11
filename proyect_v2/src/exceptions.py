"""Excepciones del sistema."""

class ScraperException(Exception):
    """Excepción base."""
    pass

class InvalidURLException(ScraperException):
    """URL inválida."""
    pass

class ExtractionException(ScraperException):
    """Error en extracción."""
    pass