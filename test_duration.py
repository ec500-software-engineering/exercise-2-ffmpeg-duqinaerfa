from pytest import approx
import main
import subprocess
import json

def ffprobe(file):
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                	'-print_format', 'json',
                                	'-show_streams',
                                	'-show_format',
                                	str(file)], universal_newlines = True)
    return json.loads(meta)

def test_duration():

    fnin = './test.mp4'

    fnout_480 = './test_480p.mp4'

    fnout_720 = './test_720p.mp4'


    info_in1 = ffprobe(fnin)

    info_out_4801 = ffprobe(fnout_480)

    info_out_7201 = ffprobe(fnout_720)


    info_in = float(info_in1['streams'][0]['duration'])

    info_out_480 = float(info_out_4801['streams'][0]['duration'])

    info_out_720 = float(info_out_7201['streams'][0]['duration'])

    assert info_in == approx(info_out_480)
    assert info_in == approx(info_out_720)


if __name__ == '__main__':
    main.convert()
    test_duration()
