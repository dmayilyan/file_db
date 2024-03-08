CREATE TABLE IF NOT EXISTS file_locations(
id integer PRIMARY KEY AUTOINCREMENT,
path_to_file text,
camera_name text DEFAULT NULL,
created_at integer);

CREATE INDEX IF NOT EXISTS idx_camera_name 
ON
file_locations (camera_name);

CREATE INDEX IF NOT EXISTS idx_date
ON
file_locations (date(created_at));
