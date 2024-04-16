class Solution:
    @staticmethod
    def find_latest_time(s: str) -> str:
        hour, minute, *_ = s.split(":")
        new_hour, new_minute = "", ""

        if hour[0] == "?" and hour[1] == "?":
            new_hour = "11"
        elif hour[1] == "?":
            if hour[0] == "0":
                new_hour = "09"
            elif hour[0] == "1":
                new_hour = "11"
        elif hour[0] == "?":
            if hour[1] == "0":
                new_hour = "10"
            elif hour[1] == "1":
                new_hour = "11"
            else:
                new_hour = "0" + hour[1]
        else:
            new_hour = hour

        if minute[0] == "?" and minute[1] == "?":
            new_minute = "59"
        elif minute[1] == "?":
            new_minute = minute[0] + "9"
        elif minute[0] == "?":
            new_minute = "5" + minute[1]
        else:
            new_minute = minute

        return f"{new_hour}:{new_minute}"


if __name__ == "__main__":
    assert Solution.find_latest_time(s="1?:?4") == "11:54"
    assert Solution.find_latest_time(s="0?:5?") == "09:59"
