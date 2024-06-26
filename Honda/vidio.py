import pyglet

vidPath = 'honda intro.mp4'
window = pyglet.window.Window()
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)

player.queue(MediaLoad)
player.play()


@window.e
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(50, 50)


pyglet.app.run()