from connection import supabase

def get_productos():
    response = supabase.table("productos").select("*").execute()
    return response.data
