# Generated by https://quicktype.io

from typing import List
from uuid import UUID
from datetime import datetime


class Configuration:
    audio_language_preference: str
    play_default_audio_track: bool
    subtitle_language_preference: str
    display_missing_episodes: bool
    grouped_folders: List[str]
    subtitle_mode: str
    display_collections_view: bool
    enable_local_password: bool
    ordered_views: List[str]
    latest_items_excludes: List[str]
    my_media_excludes: List[str]
    hide_played_in_latest: bool
    remember_audio_selections: bool
    remember_subtitle_selections: bool
    enable_next_episode_auto_play: bool

    def __init__(self, audio_language_preference: str, play_default_audio_track: bool, subtitle_language_preference: str, display_missing_episodes: bool, grouped_folders: List[str], subtitle_mode: str, display_collections_view: bool, enable_local_password: bool, ordered_views: List[str], latest_items_excludes: List[str], my_media_excludes: List[str], hide_played_in_latest: bool, remember_audio_selections: bool, remember_subtitle_selections: bool, enable_next_episode_auto_play: bool) -> None:
        self.audio_language_preference = audio_language_preference
        self.play_default_audio_track = play_default_audio_track
        self.subtitle_language_preference = subtitle_language_preference
        self.display_missing_episodes = display_missing_episodes
        self.grouped_folders = grouped_folders
        self.subtitle_mode = subtitle_mode
        self.display_collections_view = display_collections_view
        self.enable_local_password = enable_local_password
        self.ordered_views = ordered_views
        self.latest_items_excludes = latest_items_excludes
        self.my_media_excludes = my_media_excludes
        self.hide_played_in_latest = hide_played_in_latest
        self.remember_audio_selections = remember_audio_selections
        self.remember_subtitle_selections = remember_subtitle_selections
        self.enable_next_episode_auto_play = enable_next_episode_auto_play


class AccessSchedule:
    id: int
    user_id: UUID
    day_of_week: str
    start_hour: int
    end_hour: int

    def __init__(self, id: int, user_id: UUID, day_of_week: str, start_hour: int, end_hour: int) -> None:
        self.id = id
        self.user_id = user_id
        self.day_of_week = day_of_week
        self.start_hour = start_hour
        self.end_hour = end_hour


class Policy:
    is_administrator: bool
    is_hidden: bool
    is_disabled: bool
    max_parental_rating: int
    blocked_tags: List[str]
    enable_user_preference_access: bool
    access_schedules: List[AccessSchedule]
    block_unrated_items: List[str]
    enable_remote_control_of_other_users: bool
    enable_shared_device_control: bool
    enable_remote_access: bool
    enable_live_tv_management: bool
    enable_live_tv_access: bool
    enable_media_playback: bool
    enable_audio_playback_transcoding: bool
    enable_video_playback_transcoding: bool
    enable_playback_remuxing: bool
    force_remote_source_transcoding: bool
    enable_content_deletion: bool
    enable_content_deletion_from_folders: List[str]
    enable_content_downloading: bool
    enable_sync_transcoding: bool
    enable_media_conversion: bool
    enabled_devices: List[str]
    enable_all_devices: bool
    enabled_channels: List[UUID]
    enable_all_channels: bool
    enabled_folders: List[UUID]
    enable_all_folders: bool
    invalid_login_attempt_count: int
    login_attempts_before_lockout: int
    max_active_sessions: int
    enable_public_sharing: bool
    blocked_media_folders: List[UUID]
    blocked_channels: List[UUID]
    remote_client_bitrate_limit: int
    authentication_provider_id: str
    password_reset_provider_id: str
    sync_play_access: str

    def __init__(self, is_administrator: bool, is_hidden: bool, is_disabled: bool, max_parental_rating: int, blocked_tags: List[str], enable_user_preference_access: bool, access_schedules: List[AccessSchedule], block_unrated_items: List[str], enable_remote_control_of_other_users: bool, enable_shared_device_control: bool, enable_remote_access: bool, enable_live_tv_management: bool, enable_live_tv_access: bool, enable_media_playback: bool, enable_audio_playback_transcoding: bool, enable_video_playback_transcoding: bool, enable_playback_remuxing: bool, force_remote_source_transcoding: bool, enable_content_deletion: bool, enable_content_deletion_from_folders: List[str], enable_content_downloading: bool, enable_sync_transcoding: bool, enable_media_conversion: bool, enabled_devices: List[str], enable_all_devices: bool, enabled_channels: List[UUID], enable_all_channels: bool, enabled_folders: List[UUID], enable_all_folders: bool, invalid_login_attempt_count: int, login_attempts_before_lockout: int, max_active_sessions: int, enable_public_sharing: bool, blocked_media_folders: List[UUID], blocked_channels: List[UUID], remote_client_bitrate_limit: int, authentication_provider_id: str, password_reset_provider_id: str, sync_play_access: str) -> None:
        self.is_administrator = is_administrator
        self.is_hidden = is_hidden
        self.is_disabled = is_disabled
        self.max_parental_rating = max_parental_rating
        self.blocked_tags = blocked_tags
        self.enable_user_preference_access = enable_user_preference_access
        self.access_schedules = access_schedules
        self.block_unrated_items = block_unrated_items
        self.enable_remote_control_of_other_users = enable_remote_control_of_other_users
        self.enable_shared_device_control = enable_shared_device_control
        self.enable_remote_access = enable_remote_access
        self.enable_live_tv_management = enable_live_tv_management
        self.enable_live_tv_access = enable_live_tv_access
        self.enable_media_playback = enable_media_playback
        self.enable_audio_playback_transcoding = enable_audio_playback_transcoding
        self.enable_video_playback_transcoding = enable_video_playback_transcoding
        self.enable_playback_remuxing = enable_playback_remuxing
        self.force_remote_source_transcoding = force_remote_source_transcoding
        self.enable_content_deletion = enable_content_deletion
        self.enable_content_deletion_from_folders = enable_content_deletion_from_folders
        self.enable_content_downloading = enable_content_downloading
        self.enable_sync_transcoding = enable_sync_transcoding
        self.enable_media_conversion = enable_media_conversion
        self.enabled_devices = enabled_devices
        self.enable_all_devices = enable_all_devices
        self.enabled_channels = enabled_channels
        self.enable_all_channels = enable_all_channels
        self.enabled_folders = enabled_folders
        self.enable_all_folders = enable_all_folders
        self.invalid_login_attempt_count = invalid_login_attempt_count
        self.login_attempts_before_lockout = login_attempts_before_lockout
        self.max_active_sessions = max_active_sessions
        self.enable_public_sharing = enable_public_sharing
        self.blocked_media_folders = blocked_media_folders
        self.blocked_channels = blocked_channels
        self.remote_client_bitrate_limit = remote_client_bitrate_limit
        self.authentication_provider_id = authentication_provider_id
        self.password_reset_provider_id = password_reset_provider_id
        self.sync_play_access = sync_play_access


class JellyfinUser:
    name: str
    server_id: str
    server_name: str
    id: UUID
    primary_image_tag: str
    has_password: bool
    has_configured_password: bool
    has_configured_easy_password: bool
    enable_auto_login: bool
    last_login_date: datetime
    last_activity_date: datetime
    configuration: Configuration
    policy: Policy
    primary_image_aspect_ratio: int

    def __init__(self, Name: str, ServerId: str, ServerName: str, Id: UUID, PrimaryImageTag: str, HasPassword: bool, HasConfiguredPassword: bool, HasConfiguredEasyPassword: bool, EnableAutoLogin: bool, LastLoginDate: datetime, LastActivityDate: datetime, Configuration: Configuration, Policy: Policy, PrimaryImageAspectRatio: int) -> None:
        self.name = Name
        self.server_id = ServerId
        self.server_name = ServerName
        self.id = Id
        self.primary_image_tag = PrimaryImageTag
        self.has_password = HasPassword
        self.has_configured_password = HasConfiguredPassword
        self.has_configured_easy_password = HasConfiguredEasyPassword
        self.enable_auto_login = EnableAutoLogin
        self.last_login_date = LastLoginDate
        self.last_activity_date = LastActivityDate
        self.configuration = Configuration
        self.policy = Policy
        self.primary_image_aspect_ratio = PrimaryImageAspectRatio