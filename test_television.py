import pytest
from television import *

class Test:
    def setup_method(self):
        self.tv_1 = Television()

    def teardown_method(self):
        del self.tv_1

    def test_init(self):
        #testing for correct initialization values.
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        #testing details when Television object is on.
        self.tv_1.power()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        #testing details when Television object is off.
        self.tv_1.power()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        #testing details when Television object is on, volume incremented and then object is muted.
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.mute()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 0'

        #testing details when Television object is on and unmuted.
        self.tv_1.mute()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #testing details when Television object is off and muted.
        self.tv_1.power()
        self.tv_1.mute()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 1'

        #testing details when Television object is off and unmuted.
        self.tv_1.power()
        self.tv_1.mute()
        self.tv_1.power()
        self.tv_1.mute()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_channel_up(self):
        #testing details when Television object is off and channel incremented.
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #testing details when Television object is on and channel incremented.
        self.tv_1.power()
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == 'Power = True, Channel = 1, Volume = 0'

        #testing details when Television object is on, reaches the max. channel value, and is incremented.
        self.tv_1.channel_up()
        self.tv_1.channel_up()
        self.tv_1.channel_up()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        #testing details when Television object is off and channel decremented.
        self.tv_1.channel_down()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #testing details when Television object is on and channel decremented.
        self.tv_1.power()
        self.tv_1.channel_down()
        assert self.tv_1.__str__() == 'Power = True, Channel = 3, Volume = 0'

        #testing details when Television object is on, reaches min. channel value, and is decremented.
        self.tv_1.channel_down()
        self.tv_1.channel_down()
        self.tv_1.channel_down()
        assert self.tv_1.__str__()  == 'Power = True, Channel = 0, Volume = 0'

    def test_volume_up(self):
        #testing details when Television object is off and volume is incremented.
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #testing details when Television object is on and volume is incremented.
        self.tv_1.power()
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #testing details when Television object is on, muted, and volume is incremented.
        self.tv_1.mute()
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 2'

        #testing details when Television object is on, reaches max. volume value and is incremented again.
        self.tv_1.volume_up()
        self.tv_1.volume_up()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        #testing details when Television object is off and volume decremented.
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #testing details when Television object is on and volume is decremented from a non-zero value.
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.volume_up()
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #testing details when Television object is on, muted, and volume is decremented.
        self.tv_1.volume_up()
        self.tv_1.mute()
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #testing details when Television object is on, reaches min. volume value, and is decremented again.
        self.tv_1.volume_down()
        self.tv_1.volume_down()
        assert self.tv_1.__str__() == 'Power = True, Channel = 0, Volume = 0'


