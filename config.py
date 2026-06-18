"""
config.py
---------
ΟΛΑ τα IDs του server μπαίνουν εδώ. Κάθε placeholder λέει ΤΙ ΑΚΡΙΒΩΣ πρέπει να βάλεις.
Βάλε τα IDs σαν integers (χωρίς εισαγωγικά), π.χ. OWNERSHIP_ROLE_ID = 123456789012345678

Tip: Discord Developer Mode -> Right click role/channel/category -> Copy ID
"""

import os
from dotenv import load_dotenv

load_dotenv()

# =========================================================
# BOT TOKEN (μπαίνει στο .env locally, ή Environment Variable στο Render)
# =========================================================
TOKEN = os.getenv("DISCORD_TOKEN")

GUILD_ID = 000000000000000000  # PLACEHOLDER: το ID του server σου
PREFIX = "!"

# =========================================================
# ROLES
# =========================================================
OWNERSHIP_ROLE_ID        = 000000000000000000  # PLACEHOLDER
MANAGER_ROLE_ID          = 000000000000000000  # PLACEHOLDER
STAFF_ROLE_ID            = 000000000000000000  # PLACEHOLDER
DEVELOPER_ROLE_ID        = 000000000000000000  # PLACEHOLDER
CIVILIAN_MANAGER_ROLE_ID = 000000000000000000  # PLACEHOLDER
CRIMINAL_MANAGER_ROLE_ID = 000000000000000000  # PLACEHOLDER
DONATE_MANAGER_ROLE_ID   = 000000000000000000  # PLACEHOLDER
FOUNDER_ROLE_ID          = 000000000000000000  # PLACEHOLDER
ON_DUTY_ROLE_ID          = 000000000000000000  # PLACEHOLDER
WAITING_INTERVIEW_ROLE_ID = 000000000000000000  # PLACEHOLDER (μπαίνει σε accepted applicants)

# Ρόλοι που θεωρούνται "staff team" γενικά (χρησιμοποιείται σε αρκετά permission checks)
STAFF_TEAM_ROLE_IDS = [STAFF_ROLE_ID, MANAGER_ROLE_ID, OWNERSHIP_ROLE_ID]

# =========================================================
# TICKET SYSTEM #1 - SUPPORT (dropdown, 4 κατηγορίες, ξεχωριστό category η κάθε μία)
# =========================================================
TICKET_SUPPORT_CHANNEL_ID = 000000000000000000  # PLACEHOLDER: πού θα σταλεί το panel (slash command target)
TICKET_SUPPORT_BANNER_URL = "https://PLACEHOLDER-BANNER-SUPPORT.png"
TICKET_SUPPORT_THUMBNAIL_URL = "https://PLACEHOLDER-THUMBNAIL-SUPPORT.png"

CAT_TICKET_OWNERSHIP_ID = 000000000000000000  # PLACEHOLDER category
CAT_TICKET_REPORT_ID    = 000000000000000000  # PLACEHOLDER category
CAT_TICKET_SUPPORT_ID   = 000000000000000000  # PLACEHOLDER category
CAT_TICKET_BUG_ID        = 000000000000000000  # PLACEHOLDER category

# =========================================================
# TICKET SYSTEM #2 - JOBS (button, civilian + criminal, ΙΔΙΟ category και τα δύο)
# =========================================================
CAT_JOBS_ID = 000000000000000000  # PLACEHOLDER (ΚΟΙΝΟ category civilian + criminal)

TICKET_JOBS_BANNER_URL = "https://PLACEHOLDER-BANNER-JOBS.png"
TICKET_JOBS_THUMBNAIL_URL = "https://PLACEHOLDER-THUMBNAIL-JOBS.png"

# =========================================================
# TICKET SYSTEM #3 - DONATE (button, δικό του category)
# =========================================================
CAT_DONATE_ID = 000000000000000000  # PLACEHOLDER category

TICKET_DONATE_BANNER_URL = "https://PLACEHOLDER-BANNER-DONATE.png"
TICKET_DONATE_THUMBNAIL_URL = "https://PLACEHOLDER-THUMBNAIL-DONATE.png"

# Channel όπου γίνεται ping το staff team όταν ανοίγει ΟΠΟΙΟΔΗΠΟΤΕ ticket (support/jobs/donate) ή temp voice
STAFF_PING_CHANNEL_ID = 000000000000000000  # PLACEHOLDER

# =========================================================
# SUGGESTIONS
# =========================================================
SUGGESTIONS_CHANNEL_ID = 000000000000000000  # PLACEHOLDER (εδώ ο χρήστης γράφει -> γίνεται auto suggestion)

# =========================================================
# TEMP VOICE
# =========================================================
TEMP_VOICE_JOIN_CHANNEL_ID = 000000000000000000  # PLACEHOLDER ("Join to Create" channel)
TEMP_VOICE_CATEGORY_ID     = 000000000000000000  # PLACEHOLDER (εκεί δημιουργούνται τα temp channels)

# =========================================================
# STAFF ACTIVITY
# =========================================================
STAFF_ACTIVITY_VOICE_CHANNEL_ID = 000000000000000000  # PLACEHOLDER (το channel που μετράμε χρόνο)
STAFF_ACTIVITY_PANEL_CHANNEL_ID = 000000000000000000  # PLACEHOLDER (πού στέλνεται/μένει το leaderboard panel)
STAFF_ACTIVITY_LOG_CHANNEL_ID   = 000000000000000000  # PLACEHOLDER
STAFF_ACTIVITY_BANNER_URL = "https://PLACEHOLDER-BANNER-STAFFACTIVITY.png"

# =========================================================
# LOGS (Requirement 8)
# =========================================================
LOG_JOIN_LEAVE_CHANNEL_ID = 000000000000000000  # PLACEHOLDER (join + leave μαζί)
LOG_ROLES_CHANNEL_ID      = 000000000000000000  # PLACEHOLDER
LOG_CHANNELS_CHANNEL_ID   = 000000000000000000  # PLACEHOLDER (create/delete/edit channels)
LOG_MESSAGES_CHANNEL_ID   = 000000000000000000  # PLACEHOLDER (edit/delete messages)
LOG_VOICE_CHANNEL_ID      = 000000000000000000  # PLACEHOLDER
LOG_APPLICATIONS_CHANNEL_ID = 000000000000000000  # PLACEHOLDER

# Command logs (Requirement 5) - ξεχωριστό log ανά εντολή, εκτός say/say2/dmall (κοινό)
LOG_BAN_CHANNEL_ID          = 000000000000000000  # PLACEHOLDER
LOG_UNBAN_CHANNEL_ID        = 000000000000000000  # PLACEHOLDER
LOG_KICK_CHANNEL_ID         = 000000000000000000  # PLACEHOLDER
LOG_TIMEOUT_CHANNEL_ID      = 000000000000000000  # PLACEHOLDER
LOG_UNTIMEOUT_CHANNEL_ID    = 000000000000000000  # PLACEHOLDER
LOG_CLEARMESSAGES_CHANNEL_ID = 000000000000000000  # PLACEHOLDER
LOG_SAY_DMALL_CHANNEL_ID    = 000000000000000000  # PLACEHOLDER (say, say2, dmall μαζί)

# =========================================================
# APPLICATIONS (Requirement 9)
# =========================================================
APPLICATIONS_PANEL_CHANNEL_ID = 000000000000000000  # PLACEHOLDER (πού στέλνεται το panel)
APPLICATIONS_CATEGORY_ID      = 000000000000000000  # PLACEHOLDER (εκεί ανοίγουν τα application channels)
APPLICATIONS_BANNER_URL = "https://PLACEHOLDER-BANNER-APPLICATIONS.png"

# Τύποι αιτήσεων -> ερωτήσεις. Βάλε τις ερωτήσεις σου εδώ (μία λίστα string ανά τύπο).
APPLICATION_TYPES = {
    "elas": {
        "label": "ΕΛ.ΑΣ",
        "questions": [
            "PLACEHOLDER ερώτηση 1",
            "PLACEHOLDER ερώτηση 2",
        ],
    },
    "ekab": {
        "label": "ΕΚΑΒ",
        "questions": [
            "PLACEHOLDER ερώτηση 1",
        ],
    },
    "army": {
        "label": "Στρατός",
        "questions": [
            "PLACEHOLDER ερώτηση 1",
        ],
    },
    "staff": {
        "label": "Staff",
        "questions": [
            "PLACEHOLDER ερώτηση 1",
        ],
    },
    "manager": {
        "label": "Manager",
        "questions": [
            "PLACEHOLDER ερώτηση 1",
        ],
    },
}

# =========================================================
# SERVER STATUS (Requirement 10) - voice channels που λειτουργούν ως "οθόνες"
# =========================================================
STATUS_MEMBERS_CHANNEL_ID = 000000000000000000  # PLACEHOLDER (π.χ. "👥 Members: 120")
STATUS_ONLINE_CHANNEL_ID  = 000000000000000000  # PLACEHOLDER
STATUS_BOOSTS_CHANNEL_ID  = 000000000000000000  # PLACEHOLDER
STATUS_BOTS_CHANNEL_ID    = 000000000000000000  # PLACEHOLDER

# =========================================================
# ΓΕΝΙΚΑ
# =========================================================
EMBED_COLOR = 0x2B2D31  # default χρώμα για logs/embeds, άλλαξέ το όπως θες
