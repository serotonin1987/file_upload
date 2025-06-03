import asyncio
import time

async def task_runner(name, delay, action_description):
    start_time = time.time()
    print(f"[{time.strftime('%H:%M:%S', time.localtime(start_time))}] Начало {action_description}...")
    await asyncio.sleep(delay)
    end_time = time.time()
    print(f"[{time.strftime('%H:%M:%S', time.localtime(end_time))}] {action_description} завершена. Длительность: {end_time - start_time:.2f} секунд.")
    return f"Результат {name}"

async def main():
    program_start_time = time.time()
    print(f"[{time.strftime('%H:%M:%S', time.localtime(program_start_time))}] Программа запущена.")

    download_task = task_runner("загрузки", 3, "загрузки файла")
    process_task = task_runner("обработки", 2, "обработки данных")

    results = await asyncio.gather(download_task, process_task)

    print(f"\n{results[0]}")
    print(f"{results[1]}")

    program_end_time = time.time()
    print(f"[{time.strftime('%H:%M:%S', time.localtime(program_end_time))}] Программа завершена.")
    print(f"Общая продолжительность работы программы: {program_end_time - program_start_time:.2f} секунд.")

if __name__ == "__main__":
    asyncio.run(main())
