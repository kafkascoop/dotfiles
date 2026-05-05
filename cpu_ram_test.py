import multiprocessing
import time
import hashlib

# -------- CPU STRESS WITH AUTO-STOP --------
def cpu_stress(duration):
    # This process will keep hashing until the timer runs out
    stop_at = time.time() + duration
    while time.time() < stop_at:
        hashlib.sha256(b"stress_test").hexdigest()

# -------- RAM TEST WITH CLEANUP --------
def run_stability_test(ram_mb, duration):
    print(f"🚀 Starting {duration} second stability test...")
    
    # 1. Start CPU Load on all cores
    processes = []
    core_count = multiprocessing.cpu_count()
    for i in range(core_count):
        p = multiprocessing.Process(target=cpu_stress, args=(duration,))
        p.daemon = True # Ensures they close if the main script exits
        p.start()
        processes.append(p)
    
    print(f"🔥 CPU: {core_count} cores active.")

    # 2. Allocate RAM
    print(f"📦 RAM: Allocating {ram_mb} MB...")
    try:
        # Create a single block of memory
        data = bytearray(ram_mb * 1024 * 1024)
        
        # Simple write to ensure the OS actually commits the memory
        for i in range(0, len(data), 4096): # Jump in pages to be faster
            data[i] = 1
            
        print("✅ Memory allocated. Holding load...")
        
        # 3. Wait for the timer
        time.sleep(duration)
        
    except MemoryError:
        print("❌ Failed to allocate that much RAM! Try a smaller number.")
    finally:
        # 4. Cleanup
        print("🧹 Cleaning up and releasing resources...")
        for p in processes:
            p.terminate()
        print("🏁 Test Finished.")

# -------- MAIN --------
if __name__ == "__main__":
    # --- ADJUST THESE NUMBERS ---
    SECONDS_TO_RUN = 60    # Stop point: 1 minute
    RAM_SIZE_MB = 2048     # Amount of RAM to fill (2GB)
    # ----------------------------

    run_stability_test(RAM_SIZE_MB, SECONDS_TO_RUN)
  
