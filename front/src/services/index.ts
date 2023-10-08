/* eslint-disable @typescript-eslint/no-explicit-any */
const DB_TOKEN = "metadata_token";

const COLLECTION_MUSIC = "music";

class Database {
  getMetadata() {
    const metadata = localStorage.getItem(DB_TOKEN);
    return JSON.parse(metadata || "{}");
  }

  setMetadata(data: object) {
    const metadata = JSON.stringify(data);
    localStorage.setItem(DB_TOKEN, metadata);
  }

  getOne(id: string | null, collection: string) {
    const db = this.getMetadata();
    const records = Array.from(db[collection] || []);

    const key = !id ? Math.floor(Math.random() * records.length) : id;

    return records.find((e: any) => (e.id = key));
  }

  getMany(collection: string) {
    const db = this.getMetadata();
    return Array.from(db[collection]);
  }
}

class Api {
  constructor(private readonly db: Database) {}

  getMusic() {
    return this.db.getOne(null, COLLECTION_MUSIC);
  }

  getMusicRecords(id: string) {
    const allRecords = this.db.getMany(COLLECTION_MUSIC);
    const currentRecord = allRecords.find((e: any) => e.id == id);

    if (!currentRecord) {
      throw new Error("music not found!");
    }

    const listRecords = [currentRecord];

    while (listRecords.length < 4) {
      const ramdomIdx = Math.floor(Math.random() * allRecords.length);
      const randomRecord: any = allRecords.findIndex((e) => e === ramdomIdx);

      const selectedRecord = listRecords.find(
        (e: any) => e.id === randomRecord.id
      );
      if (selectedRecord) {
        listRecords.push(selectedRecord);
      }
    }
  }

  verifyMusic(idCurrent: string, idTarget: string) {
    return {
      isSuccess: idCurrent === idTarget,
    };
  }
}

const service = new Api(new Database());

export default service;
