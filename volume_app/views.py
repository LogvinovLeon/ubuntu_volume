import subprocess

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View


class VolumeView(View):
    def get(self, request):
        print({"volume": self.get_volume()})
        return render(request, 'volume.html', {"volume": self.get_volume()})

    def post(self, request):
        data = dict(self.request.POST.items())
        volume = int(data.pop("volume", 0))
        assert (0 <= volume <= 100)
        self.set_volume(volume)
        return JsonResponse({"volume": self.get_volume()})

    def get_volume(self):
        task = subprocess.Popen("echo `(pactl list sinks | grep \"Volume: 0\")| awk '{print $3}'`",
                                shell=True, stdout=subprocess.PIPE)
        data = task.stdout.read()
        print(data)
        return int(data[:-2])

    def set_volume(self, volume):
        subprocess.call(["pactl", "set-sink-volume", "0", str(volume) + "%"])
