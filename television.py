class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None :
        """
        Initializes a Television object.
        """

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power status of a Television object.
        """

        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Toggle the mute status of a Television object.
        """

        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Increments channel number of a Television object. If the channel number is the
        maximum, loops to minimum channel number.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrements channel number of a Television object. If the channel number is the
        minimum, loops to maximum channel number.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increments volume for Television object. If object is muted, will
        unmute object.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrement volume for a Television object. If object is muted, will
        unmute object.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False

            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Overrides print method to return power, channel and volume information.

        :return: string containing current power, channel and volume info.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'