import instaloader

def get_not_following_back(username):
    L = instaloader.Instaloader()

    L.load_session_from_file(username)

    profile = instaloader.Profile.from_username(L.context, username)

    print("Fetching followers...")
    followers = {f.username for f in profile.get_followers()}

    print("Fetching following...")
    following = {f.username for f in profile.get_followees()}

    not_following_back = following - followers

    print("\nAccounts not following you back:\n")

    for user in sorted(not_following_back):
        print(user)

    print(f"\nTotal: {len(not_following_back)} accounts")


username = input("Enter your Instagram username: ")

get_not_following_back(username)
