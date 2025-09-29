import asyncio

class BatchFetcher:
    def __init__(self, database):
        self.database = database

    async def fetch_records(self, datum_id):
        records = []
        for datum in datum_id:
            records.append(self.database.async_fetch(datum))

        return await asyncio.gather(*records)

# import asyncio

class BatchFetcher:
    # The `database` has an `async_fetch` method
    # that you should use in your code. This method
    # takes in a record id and returns a record.
    def __init__(self, database):
        self.database = database
        # self.records = []

    async def fetch(self, datum, records):
        return await records.append(self.database[datum])
        

    async def fetch_records(self):
        # First, we need to prepare the coroutiunes
        records = []
        datum = [self.fetch(i, records) for i in self.database]
        data = await asyncio.gather(*datum)
        return data
        
    
database = {"A": {"a": 45}}
fecther = BatchFetcher(database)
print(fecther.fetch_records)

# # Welcome to our Python playground!

# import asyncio
# import time


# # Here we fake the download of a large file by sleeping 1 second.
# async def download_large_file(file_name, a_list):
#     await asyncio.sleep(1)
#     a_list.append(file_name)
#     print(f"{file_name} was downloaded successfully")
#     return f"{file_name}: OK"


# # These are the files to download. Since each file takes 1 second
# # to download, it would take 5 seconds without using asyncio.
# FILES_TO_DOWNLOAD = [
#     "textures.zip",
#     "models.zip",
#     "physics_engine.exe",
#     "game.exe",
#     "achievements.exe",
# ]


# async def main():
#     a_list = []
#     start_time = time.time()
#     downloads = [download_large_file(file_name, a_list) for file_name in FILES_TO_DOWNLOAD]
#     download_statuses = await asyncio.gather(*downloads)
#     total_time = time.time() - start_time
#     print(f"Finished downloading {len(download_statuses)} files in {total_time} seconds!", a_list)


# asyncio.run(main())


    


