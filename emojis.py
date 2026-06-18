"""
emojis.py
---------
Custom emojis χωρισμένα ανά κατηγορία.

ΠΩΣ ΤΟ ΣΥΜΠΛΗΡΩΝΕΙΣ:
- Static emoji:   "<:name:ID>"
- Animated emoji: "<a:name:ID>"   (πρόσεξε το "a" πριν τα δύο κόλον)

Το "name" δεν χρειάζεται να ταιριάζει 100% με το πραγματικό όνομα του emoji,
αλλά καλό είναι να το αφήσεις ίδιο για ευκολία. Το μόνο που μετράει στην
εμφάνιση είναι το σωστό ID.

Χρήση μέσα στον κώδικα:
    from emojis import emoji
    emoji("tickets", "close")
"""

EMOJIS = {
    "tickets": {
        "ownership": "<:ownership:000000000000000000>",
        "report": "<:report:000000000000000000>",
        "support": "<:support:000000000000000000>",
        "bug": "<:bug:000000000000000000>",
        "close": "<:close:000000000000000000>",
        "ping": "<:ping:000000000000000000>",
        "ticket": "<:ticket:000000000000000000>",
    },
    "jobs": {
        "civilian": "<:civilian:000000000000000000>",
        "criminal": "<:criminal:000000000000000000>",
    },
    "donate": {
        "donate": "<a:donate:000000000000000000>",  # παράδειγμα animated
    },
    "suggestions": {
        "upvote": "<:upvote:000000000000000000>",
        "downvote": "<:downvote:000000000000000000>",
    },
    "moderation": {
        "ban": "<:ban:000000000000000000>",
        "unban": "<:unban:000000000000000000>",
        "kick": "<:kick:000000000000000000>",
        "timeout": "<:timeout:000000000000000000>",
        "untimeout": "<:untimeout:000000000000000000>",
        "clear": "<:clear:000000000000000000>",
    },
    "voice": {
        "join": "<:voice_join:000000000000000000>",
        "leave": "<:voice_leave:000000000000000000>",
        "temp": "<:temp_voice:000000000000000000>",
    },
    "staff_activity": {
        "on_duty": "<a:on_duty:000000000000000000>",
        "off_duty": "<:off_duty:000000000000000000>",
        "leaderboard": "<:leaderboard:000000000000000000>",
    },
    "applications": {
        "elas": "<:elas:000000000000000000>",
        "ekab": "<:ekab:000000000000000000>",
        "army": "<:army:000000000000000000>",
        "staff": "<:staff:000000000000000000>",
        "manager": "<:manager:000000000000000000>",
        "accept": "<:accept:000000000000000000>",
        "deny": "<:deny:000000000000000000>",
        "apply": "<:apply:000000000000000000>",
        "send": "<:send:000000000000000000>",
        "ping_staff": "<:ping_staff:000000000000000000>",
    },
    "status": {
        "members": "<:members:000000000000000000>",
        "online": "<:online:000000000000000000>",
        "boost": "<a:boost:000000000000000000>",
        "bots": "<:bots:000000000000000000>",
    },
    "panel": {
        "list": "<:list:000000000000000000>",
    },
}


def emoji(category: str, name: str) -> str:
    """Επιστρέφει το emoji string. Αν δεν βρεθεί, επιστρέφει κενό string (δεν σκάει το bot)."""
    try:
        return EMOJIS[category][name]
    except KeyError:
        return ""
