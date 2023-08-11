import AudiLib
a = AudiLib.audio(10)
a.makeTone(500,1)
a.addTone(300,1)
a.addTone(0.1,1)
a.export("DemoAudio")
a.showForm()