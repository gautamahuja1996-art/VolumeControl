from flask import Flask, render_template, redirect, request

#pycaw code
import pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on', methods = ['POST'])
def on():
    if request.method == 'POST':
        volume.SetMasterVolumeLevelScalar(1.0, None)
        return redirect('/')
    
@app.route('/off', methods = ['POST'])
def off():
    if request.method == 'POST':
        volume.SetMasterVolumeLevelScalar(0.0, None)
        return redirect('/')
    
if __name__ == '__main__':
    app.run()
