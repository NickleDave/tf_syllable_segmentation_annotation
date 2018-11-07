"""parses [SPECTROGRAM] section of config"""
from collections import namedtuple


SpectConfig = namedtuple('SpectConfig', ['fft_size',
                                         'step_size',
                                         'freq_cutoffs',
                                         'thresh',
                                         'transform_type'])


def parse_spect_config(config):
    """parse [SPECTROGRAM] section of config.ini file

    Parameters
    ----------
    config : ConfigParser
        containing config.ini file already loaded by parse function

    Returns
    -------
    spect_config : namedtuple
        with fields:
            fft_size
            step_size
            freq_cutoffs
            thresh
            transform_type
    """
    fft_size = int(config['SPECTROGRAM']['fft_size'])
    step_size = int(config['SPECTROGRAM']['step_size'])
    freq_cutoffs = [float(element)
                    for element in
                    config['SPECTROGRAM']['freq_cutoffs'].split(',')]

    if config.has_option('SPECTROGRAM', 'thresh'):
        thresh = float(config['SPECTROGRAM']['thresh'])
    else:
        thresh = None

    if config.has_option('SPECTROGRAM', 'transform_type'):
        transform_type = config['SPECTROGRAM']['transform_type']
        valid_transform_types = {'log_spect', 'log_spect_plus_one'}
        if config['SPECTROGRAM']['transform_type'] not in valid_transform_types:
            raise ValueError('Value for `transform_type`, {}, in [SPECTROGRAM] '
                             'section of .ini file is not recognized. Must be one '
                             'of the following: {}'
                             .format(spect_params['transform_type'],
                                     valid_transform_types))
    else:
        transform_type = None

    return SpectConfig(fft_size,
                       step_size,
                       freq_cutoffs,
                       thresh,
                       transform_type)
