{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1fe3935c-befd-4fef-baf1-befd9c91571b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dataset URL: https://www.kaggle.com/datasets/ankitbansal06/retail-orders\n",
      "License(s): CC0-1.0\n",
      "Downloading orders.csv.zip to C:\\Users\\rahit\\Documents\\SQL+Python\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "  0%|          | 0.00/200k [00:00<?, ?B/s]\n",
      "100%|##########| 200k/200k [00:00<00:00, 499kB/s]\n",
      "100%|##########| 200k/200k [00:00<00:00, 488kB/s]\n"
     ]
    }
   ],
   "source": [
    "#import libraries\n",
    "#!pip install kaggle\n",
    "import kaggle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85dec97e-2fb3-4449-9d40-dae8499948f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#download a dataset using kaggle api\n",
    "!kaggle datasets download ankitbansal06/retail-orders -f orders.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3e41483c-e340-4ca8-a6d7-bce505542b0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#extract file from zip file\n",
    "import zipfile\n",
    "zip_ref=zipfile.ZipFile('orders.csv.zip')\n",
    "zip_ref.extractall() #extract file to dir\n",
    "zip_ref.close() #close file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1ec59db1-943d-4c97-89c0-f09c1e6d9663",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Second Class', 'Standard Class', nan, 'First Class', 'Same Day'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#read data from the file and handle null values\n",
    "import pandas as pd\n",
    "df=pd.read_csv('orders.csv',na_values=['Not Available','unknown'])\n",
    "#df.head(20)\n",
    "df['Ship Mode'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "ddbfd8e4-1368-4c88-ba59-fffaf1deb792",
   "metadata": {},
   "outputs": [],
   "source": [
    "#rename column names ,make them lowercase and replace space with underscore\n",
    "#df\n",
    "#df.rename(columns={'Order Id':'order_id','City':'city'}) #this is not a good practice to rename each and every column\n",
    "#df.columns=df.columns.str.lower()\n",
    "#df.columns=df.columns.str.replace(' ','_')\n",
    "#df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "966c7c47-7d4d-43c0-bccc-be202f79fc53",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>order_id</th>\n",
       "      <th>order_date</th>\n",
       "      <th>ship_mode</th>\n",
       "      <th>segment</th>\n",
       "      <th>country</th>\n",
       "      <th>city</th>\n",
       "      <th>state</th>\n",
       "      <th>postal_code</th>\n",
       "      <th>region</th>\n",
       "      <th>category</th>\n",
       "      <th>sub_category</th>\n",
       "      <th>product_id</th>\n",
       "      <th>cost_price</th>\n",
       "      <th>list_price</th>\n",
       "      <th>quantity</th>\n",
       "      <th>discount_percent</th>\n",
       "      <th>discount</th>\n",
       "      <th>sale_price</th>\n",
       "      <th>profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>2023-03-01</td>\n",
       "      <td>Second Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Henderson</td>\n",
       "      <td>Kentucky</td>\n",
       "      <td>42420</td>\n",
       "      <td>South</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Bookcases</td>\n",
       "      <td>FUR-BO-10001798</td>\n",
       "      <td>240</td>\n",
       "      <td>260</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>5.2</td>\n",
       "      <td>254.8</td>\n",
       "      <td>14.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>2023-08-15</td>\n",
       "      <td>Second Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Henderson</td>\n",
       "      <td>Kentucky</td>\n",
       "      <td>42420</td>\n",
       "      <td>South</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Chairs</td>\n",
       "      <td>FUR-CH-10000454</td>\n",
       "      <td>600</td>\n",
       "      <td>730</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>21.9</td>\n",
       "      <td>708.1</td>\n",
       "      <td>108.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>2023-01-10</td>\n",
       "      <td>Second Class</td>\n",
       "      <td>Corporate</td>\n",
       "      <td>United States</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>California</td>\n",
       "      <td>90036</td>\n",
       "      <td>West</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Labels</td>\n",
       "      <td>OFF-LA-10000240</td>\n",
       "      <td>10</td>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>0.5</td>\n",
       "      <td>9.5</td>\n",
       "      <td>-0.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>2022-06-18</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Fort Lauderdale</td>\n",
       "      <td>Florida</td>\n",
       "      <td>33311</td>\n",
       "      <td>South</td>\n",
       "      <td>Furniture</td>\n",
       "      <td>Tables</td>\n",
       "      <td>FUR-TA-10000577</td>\n",
       "      <td>780</td>\n",
       "      <td>960</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>19.2</td>\n",
       "      <td>940.8</td>\n",
       "      <td>160.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>2022-07-13</td>\n",
       "      <td>Standard Class</td>\n",
       "      <td>Consumer</td>\n",
       "      <td>United States</td>\n",
       "      <td>Fort Lauderdale</td>\n",
       "      <td>Florida</td>\n",
       "      <td>33311</td>\n",
       "      <td>South</td>\n",
       "      <td>Office Supplies</td>\n",
       "      <td>Storage</td>\n",
       "      <td>OFF-ST-10000760</td>\n",
       "      <td>20</td>\n",
       "      <td>20</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>1.0</td>\n",
       "      <td>19.0</td>\n",
       "      <td>-1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   order_id  order_date       ship_mode    segment        country  \\\n",
       "0         1  2023-03-01    Second Class   Consumer  United States   \n",
       "1         2  2023-08-15    Second Class   Consumer  United States   \n",
       "2         3  2023-01-10    Second Class  Corporate  United States   \n",
       "3         4  2022-06-18  Standard Class   Consumer  United States   \n",
       "4         5  2022-07-13  Standard Class   Consumer  United States   \n",
       "\n",
       "              city       state  postal_code region         category  \\\n",
       "0        Henderson    Kentucky        42420  South        Furniture   \n",
       "1        Henderson    Kentucky        42420  South        Furniture   \n",
       "2      Los Angeles  California        90036   West  Office Supplies   \n",
       "3  Fort Lauderdale     Florida        33311  South        Furniture   \n",
       "4  Fort Lauderdale     Florida        33311  South  Office Supplies   \n",
       "\n",
       "  sub_category       product_id  cost_price  list_price  quantity  \\\n",
       "0    Bookcases  FUR-BO-10001798         240         260         2   \n",
       "1       Chairs  FUR-CH-10000454         600         730         3   \n",
       "2       Labels  OFF-LA-10000240          10          10         2   \n",
       "3       Tables  FUR-TA-10000577         780         960         5   \n",
       "4      Storage  OFF-ST-10000760          20          20         2   \n",
       "\n",
       "   discount_percent  discount  sale_price  profit  \n",
       "0                 2       5.2       254.8    14.8  \n",
       "1                 3      21.9       708.1   108.1  \n",
       "2                 5       0.5         9.5    -0.5  \n",
       "3                 2      19.2       940.8   160.8  \n",
       "4                 5       1.0        19.0    -1.0  "
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#derive new columns discount,sale price and profit\n",
    "#df['discount']=df['list_price']*df['discount_percent']*0.01\n",
    "#df['sale_price']=df['list_price']-df['discount']\n",
    "df['profit']=df['sale_price']-df['cost_price']\n",
    "df.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "e5b73258-42cd-476e-bde1-c3881d54ec82",
   "metadata": {},
   "outputs": [],
   "source": [
    "#convert order date from object datatype to datetime\n",
    "df['order_date']=pd.to_datetime(df['order_date'],format='%Y-%m-%d')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "ea4836fa-4dcf-4c8d-83af-208379322cd8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#drop cost price , list price,discount columns\n",
    "df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "e8a57c47-86e6-4c98-b73f-a7fca4e0afae",
   "metadata": {},
   "outputs": [],
   "source": [
    "#load the data into sql server using replace option\n",
    "import sqlalchemy as sal\n",
    "engine=sal.create_engine('mssql://RahityaGovindu/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')\n",
    "conn=engine.connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "0dd7d6e6-bd75-492b-9d04-e248a5672ffb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "38"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#load data into sql using append option\n",
    "df.to_sql('df_orders',con=conn,index=False,if_exists='append')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "178cb12b-83ad-4a08-bbfc-169843d5b762",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23a38e0e-b64e-4de4-86a1-57214dc73050",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f8a5c82-b5fa-462d-9f36-6d66e0c68301",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
