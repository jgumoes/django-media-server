# Media Server

## What?
This is (going to be) a media server written in Django. The intention is to deploy it to a raspberry pi (or some other mini computer), and be able to access everything on the go. But why stop there? Why not overcomplicate things?

### Roadmap

* make a script that lists all music files on Django admin
* add a play button to Django admin
* filter songs by artist/album/genre etc.
* make a frontend! (React or Django templates? I don't know!)
* extend functionality to videos/movies

*But why stop there?*

These last steps are where the project gets really ambitious:
* create an API server to deliver content
* Implement casting.

I want to stream my music and videos and DVD rips to my television, and I want it to work regardless of what the internet router is doing (see below). I want to have a raspberry pi/dongle computer attached to the TV and HiFi, and use my phone to tell it which movies / songs to play.

## Why?
My music folder on my computer is currently 189 Gb and has over 16K files. Most of it is unlistened to, though. Thing is, I've always found it really awkward listening on my laptop, especially when I'm driving or on a walk. More importantly, there is just too much to fit on my phone. So many of the free Bandcamp albums remain unlistened.

It's not just the music though, what if I want to watch a legally-acquired episode of Adventure Time on my break at work? I shouldn't have to plan ahead when we have the technology to stream!

There's a final issue that has not been addressed in the tech industry: internet connections aren't 100% reliable. I want this system to work on local host in case of outages, but [modern routers are increasingly incapable of handling the sheer number of devices in the modern home, and especially for multiple occupancy households](https://youtu.be/_IzyJTcnPu8?t=45). As t currently stands, none of my smart devices are functional because they just can't connect to the WiFi.
The connectivity issues can be fixed simply by accommodating multiple WiFi connections. That way, I could connect to the router when it's working, connect to it when it reverts itself to factory defaults, and can connect to my phone's hotspot when the internet is down.
Making my own media casting solution will ensure reliable functionality.
(Note to self: insert LTT video)

*But why not just find an existing media server? Wanting to stream your own music and videos is pretty common?*

No. Shut up. It's not the same. Did you even read the Roadmap?


## When?
OMG I'm working on it, calm down already!
