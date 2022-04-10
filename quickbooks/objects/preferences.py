from six import python_2_unicode_compatible
from .base import QuickbooksReadOnlyObject, QuickbooksBaseObject, Ref


@python_2_unicode_compatible
class AccountingInfoPrefs(QuickbooksBaseObject):
    def __init__(self):
        super(AccountingInfoPrefs, self).__init__()

        self.FirstMonthOfFiscalYear = ""
        self.UseAccountNumbers = ""
        self.TaxYearMonth = ""
        self.ClassTrackingPerTxn = ""
        self.TrackDepartments = ""
        self.TaxForm = ""
        self.CustomerTerminology = ""
        self.BookCloseDate = ""
        self.DepartmentTerminology = ""
        self.ClassTrackingPerTxnLine = ""

    def __str__(self):
        return self.value


@python_2_unicode_compatible
class Preferences(QuickbooksReadOnlyObject):
    """
    QBO definition: The Preferences resource represents a set of
    company preferences that control application behavior in
    QuickBooks Online. They are mostly exposed as read-only through
    the Preferences endpoint with only a very small subset of them
    available as writable. Preferences are not necessarily honored
    when making requests via the QuickBooks API because a lot of
    them control UI behavior in the application and may not be
    applicable for apps.
    
    Some attributes may exist in both CompanyInfo and the Preferences
    entities. We are including this section to be able to access
    the BookCloseDate information.

    Note: Preferences cannot be created or updated via the Quickbooks API
    """

    class_dict = {
        "AccountingInfoPrefs": AccountingInfoPrefs,
    }

    qbo_object_name = "Preferences"

    def __init__(self):
        super(Preferences, self).__init__()

        self.Id = None

    def __str__(self):
        return "Preferences"

    def to_ref(self):
        ref = Ref()

        ref.type = self.qbo_object_name
        ref.value = self.Id

        return ref
