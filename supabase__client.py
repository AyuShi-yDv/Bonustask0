from supabase import create_client
import os

SUPABASE_URL = os.getenv("https://tecbphkrjbinmajymwux.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRlY2JwaGtyamJpbm1hanltd3V4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjUwMjI3MjgsImV4cCI6MjA4MDU5ODcyOH0.8DuIHxMntykkL384s37r-xI4mQrByDITsgjYz4etoFQ")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
