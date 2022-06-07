class Navigation(object):
    """
    Navigation class for RINEX Observation (*.*n/p) files
    """

    def __init__(self, epoch=None, navigation=None, version=None, alphalist=None, betalist=None):
        self.epoch = epoch
        self.navigation = navigation
        self.version = version
        self.alphalist = alphalist
        self.betalist = betalist