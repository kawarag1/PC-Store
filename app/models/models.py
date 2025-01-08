from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.utils.articlesgen import generate_articul, ItemsTypes
import uuid

from sqlalchemy import *

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    login:Mapped[str] = mapped_column(String(255), unique = True)
    password:Mapped[str] = mapped_column(String(255))
    email:Mapped[str] = mapped_column(String(255), unique = True)
    name:Mapped[str] = mapped_column(String(255), nullable = True)
    surname:Mapped[str] = mapped_column(String(255), nullable = True)
    patronymic:Mapped[str] = mapped_column(String(255) ,nullable = True)


    orders:Mapped["Order"] = relationship("Order", back_populates = "users")



class Basket(Base):
    __tablename__ = "Basket"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey("Users.id"))
    cpu_id:Mapped[int] = mapped_column(Integer, ForeignKey("CPU.id"), nullable = True)
    gpu_id:Mapped[int] = mapped_column(Integer, ForeignKey("GPU.id"), nullable = True)
    ram_id:Mapped[int] = mapped_column(Integer, ForeignKey("RAM.id"), nullable = True)
    motherboard_id:Mapped[int] = mapped_column(Integer, ForeignKey("Motherboards.id"), nullable = True)
    m2_id:Mapped[int] = mapped_column(Integer, ForeignKey("M2_SSDs.id"), nullable = True)
    ssd_id:Mapped[int] = mapped_column(Integer, ForeignKey("SSDs.id"), nullable = True)
    hdd_id:Mapped[int] = mapped_column(Integer, ForeignKey("HDDs.id"), nullable = True)
    case_id:Mapped[int] = mapped_column(Integer, ForeignKey("PC_Cases.id"), nullable = True)
    cooler_id:Mapped[int] = mapped_column(Integer, ForeignKey("Coolers.id"), nullable = True)
    pu_id:Mapped[int] = mapped_column(Integer, ForeignKey("Power_Units.id"), nullable = True)
    # пока не забыл. корзина будет работать как, получается здесь будут поля всех товаров, типо products, cpu, gpu и так далее, 
    # каждое поле таблицы будет nullable = True. когда будет нажиматься кнопка добавления в таблицу, то будет регистрироваться новая запись в таблице с id юзера и артиклем товара.
    # по артиклю товара апишка будет понимать в какой столбец добавлять id или артикул.
    

    cpus:Mapped["CPU"] = relationship("CPU", back_populates = "baskets")
    gpus:Mapped["GPU"] = relationship("GPU", back_populates = "baskets")
    rams:Mapped["RAM"] = relationship("RAM", back_populates = "baskets")
    motherboards:Mapped["Motherboard"] = relationship("Motherboard", back_populates = "baskets")
    m2_ssdS:Mapped["M2_SSD"] = relationship("M2_SSD", back_populates = "baskets")
    ssdS:Mapped["SSD"] = relationship("SSD", back_populates = "baskets")
    hddS:Mapped["HDD"] = relationship("HDD", back_populates = "baskets")
    cases:Mapped["PC_CASE"] = relationship("PC_CASE", back_populates = "baskets")
    coolers:Mapped["Cooler"] = relationship("Cooler", back_populates = "baskets")
    puS:Mapped["POWER_UNIT"] = relationship("POWER_UNIT", back_populates = "baskets")

    

class Order(Base):
    __tablename__ = "Orders"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey("Users.id"))
    category_id:Mapped[int] = mapped_column(Integer ,ForeignKey("Categories.id"))
    

    users:Mapped["User"] = relationship("User", back_populates = "orders")
    categories:Mapped["Category"] = relationship("Category", back_populates = "orders")




class Category(Base):
    __tablename__ = "Categories"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    # выполнен, в обработке и тд наверн

    orders:Mapped["Order"] = relationship("Order", back_populates = "categories") 
    # products:Mapped["Order"] = relationship("Product", back_populates = "categories")




class Product(Base):
    __tablename__ = "Products"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    cost:Mapped[Numeric] = mapped_column(Numeric(10,2))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.PC))
    cpu_id:Mapped[int] = mapped_column(Integer, ForeignKey("CPU.id"))
    gpu_id:Mapped[int] = mapped_column(Integer, ForeignKey("GPU.id"))
    ram_id:Mapped[int] = mapped_column(Integer, ForeignKey("RAM.id"))
    ram_quantitiy_id:Mapped[int] = mapped_column(Integer, ForeignKey("RAM_Quantities.id"))
    motherboard_id:Mapped[int] = mapped_column(Integer, ForeignKey("Motherboards.id"))
    m2_id:Mapped[int] = mapped_column(Integer, ForeignKey("M2_SSDs.id"), nullable = True)
    ssd_id:Mapped[int] = mapped_column(Integer, ForeignKey("SSDs.id"), nullable = True)
    hdd_id:Mapped[int] = mapped_column(Integer, ForeignKey("HDDs.id"), nullable = True)
    case_id:Mapped[int] = mapped_column(Integer, ForeignKey("PC_Cases.id"))
    cooler_id:Mapped[int] = mapped_column(Integer, ForeignKey("Coolers.id"))
    pu_id:Mapped[int] = mapped_column(Integer, ForeignKey("Power_Units.id"))
    image:Mapped[str] = mapped_column(String(255))

    # дописать
    cpus:Mapped["CPU"] = relationship("CPU", back_populates = "products")
    gpus:Mapped["GPU"] = relationship("GPU", back_populates = "products")
    rams:Mapped["RAM"] = relationship("RAM", back_populates = "products")
    ram_quantities:Mapped["RAM_Quantity"] = relationship("RAM_Quantity", back_populates = "products")
    motherboards:Mapped["Motherboard"] = relationship("Motherboard", back_populates = "products")
    m2_ssdS:Mapped["M2_SSD"] = relationship("M2_SSD", back_populates = "products")
    ssdS:Mapped["SSD"] = relationship("SSD", back_populates = "products")
    hddS:Mapped["HDD"] = relationship("HDD", back_populates = "products")
    cases:Mapped["PC_CASE"] = relationship("PC_CASE", back_populates = "products")
    coolers:Mapped["Cooler"] = relationship("Cooler", back_populates = "products")
    puS:Mapped["POWER_UNIT"] = relationship("POWER_UNIT", back_populates = "products")
    # categories:Mapped["Category"] = relationship("Category", back_populates = "products")





class CPU(Base):
    __tablename__ = "CPU"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))
    cost:Mapped[int] = mapped_column(Numeric(10,2))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.CPU))
    image:Mapped[str] = mapped_column(String(255))
    cpu_specs_id:Mapped[int] = mapped_column(Integer, ForeignKey("CPU_Specs.id"))

    specs: Mapped["CPU_SPECS"] = relationship("CPU_SPECS", back_populates = "cpus")
    products: Mapped["Product"] = relationship("Product", back_populates = "cpus")
    manufacturers: Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = "cpus")
    baskets:Mapped["Basket"] = relationship("Basket", back_populates = "cpus")
    

class CPU_SPECS(Base):
    __tablename__ = "CPU_Specs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    frequency:Mapped[Numeric] = mapped_column(Numeric(10,2))
    core_count:Mapped[int] = mapped_column(Integer)
    flow_count:Mapped[int] = mapped_column(Integer)
    cache:Mapped[int] = mapped_column(Integer)
    tdp:Mapped[int] = mapped_column(Integer)
    socket_id:Mapped[int] = mapped_column(Integer, ForeignKey("Sockets.id"))
    
    sockets:Mapped["Socket"] = relationship("Socket", back_populates = "cpus_specs")
    cpus:Mapped["CPU"] = relationship("CPU", back_populates = "specs")


class GPU(Base):
    __tablename__ = "GPU"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))
    cost:Mapped[int] = mapped_column(Numeric(10,2))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.GPU))
    image:Mapped[str] = mapped_column(String(255))
    gpu_specs_id:Mapped[int] = mapped_column(Integer, ForeignKey("GPU_Specs.id"))

    specs:Mapped["GPU_SPECS"] = relationship("GPU_SPECS", back_populates = "gpus")
    products:Mapped["Product"] = relationship("Product", back_populates = "gpus")
    manufacturers:Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = "gpus")
    baskets:Mapped["Basket"] = relationship("Basket", back_populates = "gpus")


class GPU_SPECS(Base):
    __tablename__ = "GPU_Specs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    frequency:Mapped[Numeric] = mapped_column(Numeric(10,2))
    amount_video_memory:Mapped[int] = mapped_column(Integer)
    video_memory_type:Mapped[int] = mapped_column(Integer, ForeignKey("GPU_Memory_Types.id"))
    tdp:Mapped[int] = mapped_column(Integer)
    RTX_Rays:Mapped[bool] = mapped_column(Boolean, default = False)
    

    GPU_Memory_Types:Mapped["GPU_Memory_Type"] = relationship("GPU_Memory_Type", back_populates = "GPU_Specs")
    gpus:Mapped["GPU"] = relationship("GPU", back_populates = "specs")


class GPU_Memory_Type(Base):
    __tablename__ = "GPU_Memory_Types"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    
    GPU_Specs:Mapped["GPU_SPECS"] = relationship("GPU_SPECS", back_populates = "GPU_Memory_Types") 

class RAM(Base):
    __tablename__ = "RAM"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))
    cost:Mapped[int] = mapped_column(Numeric(10,2))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.RAM))
    image:Mapped[str] = mapped_column(String(255))
    ram_specs_id:Mapped[int] = mapped_column(Integer, ForeignKey("RAM_Specs.id"))

    specs:Mapped["RAM_SPECS"] = relationship("RAM_SPECS", back_populates = "rams")
    products:Mapped["Product"] = relationship("Product", back_populates = "rams")
    manufacturers:Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = "rams")
    baskets:Mapped["Basket"] = relationship("Basket", back_populates = "rams")


class RAM_SPECS(Base):
    __tablename__ = "RAM_Specs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    frequency:Mapped[int] = mapped_column(Integer)
    type_id:Mapped[int] = mapped_column(Integer, ForeignKey("RAM_Type.id"))
    radiators:Mapped[bool] = mapped_column(Boolean, default = False)

    rams:Mapped["RAM"] = relationship("RAM", back_populates = "specs")
    types:Mapped["RAM_TYPE"] = relationship("RAM_TYPE", back_populates = "ram_specs")

class RAM_TYPE(Base):
    __tablename__ = "RAM_Type"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    # записи по типу DDR5, DDR4. Не думаю что DDR3 ббудет уместна< вышла из производства

    ram_specs:Mapped["RAM_SPECS"] = relationship("RAM_SPECS", back_populates = "types")
    motherboard_specs:Mapped["Motherboard_SPECS"] = relationship("Motherboard_SPECS", back_populates = "ram_types")

class RAM_Quantity(Base):
    __tablename__ = "RAM_Quantities"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    ram_number:Mapped[str] = mapped_column(String(50))


    products:Mapped["Product"] = relationship("Product", back_populates = "ram_quantities")
    #здесь табличка тупо для размеров оперативки, получается, что будет несколько записей,
    #типо 2x8(16), 2ч16(32), 1x8, 1x16, 2x4(8)

class Motherboard(Base):
    __tablename__ = "Motherboards"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(90))
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))
    cost:Mapped[Numeric] = mapped_column(Numeric(10,2))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.MB))
    image:Mapped[str] = mapped_column(String(255))
    motherboard_specs_id:Mapped[int] = mapped_column(Integer, ForeignKey("Motherboards_Specs.id"))


    manufacturers:Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = "motherboards")
    specs:Mapped["Motherboard_SPECS"] = relationship("Motherboard_SPECS", back_populates = "motherboards")
    products:Mapped["Product"] = relationship("Product", back_populates = "motherboards")
    baskets:Mapped["Basket"] = relationship("Basket", back_populates = "motherboards")


class Motherboard_SPECS(Base):
    __tablename__ = "Motherboards_Specs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    form:Mapped[int] = mapped_column(Integer, ForeignKey("FormFactors.id"))
    chipset:Mapped[int] = mapped_column(Integer, ForeignKey("Chipsets.id"))
    socket:Mapped[int] = mapped_column(Integer, ForeignKey("Sockets.id"))
    USB_Count:Mapped[int] = mapped_column(Integer)
    SATA_Count:Mapped[int] = mapped_column(Integer)
    HDMI_Count:Mapped[int] = mapped_column(Integer)
    DisplayPort_Count:Mapped[int] = mapped_column(Integer)
    DVI_Count:Mapped[int] = mapped_column(Integer)
    VGA_Count:Mapped[int] = mapped_column(Integer)
    RAM_Count:Mapped[int] = mapped_column(Integer)
    RAM_Type_id:Mapped[int] = mapped_column(Integer, ForeignKey("RAM_Type.id"))
    M2_Slot:Mapped[int] = mapped_column(Integer, ForeignKey("M2_Sizes.id"), nullable = True)


    motherboards:Mapped["Motherboard"] = relationship("Motherboard", back_populates = "specs")
    forms:Mapped["FormFactor"] = relationship("FormFactor", back_populates = "specs")
    chipsets:Mapped["Chipset"] = relationship("Chipset", back_populates = "specs")
    sockets:Mapped["Socket"] = relationship("Socket", back_populates = "specs")
    slots:Mapped["M2_SIZE"] = relationship("M2_SIZE", back_populates = "motherboard_specs")
    ram_types:Mapped["RAM_TYPE"] = relationship("RAM_TYPE", back_populates = "motherboard_specs")

class M2_SSD(Base):
    __tablename__ = "M2_SSDs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    size:Mapped[int] = mapped_column(Integer, ForeignKey("M2_Sizes.id"))
    cost:Mapped[Numeric] = mapped_column(Numeric(10,2))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.M2))
    image:Mapped[str] = mapped_column(String(255))
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))
    m2_ssd_specs_id:Mapped[int] = mapped_column(Integer, ForeignKey("M2_SSD_Specs.id"))

    m2Size:Mapped["M2_SIZE"] = relationship("M2_SIZE", back_populates = "m2SSD")
    specs:Mapped["M2_SSD_SPECS"] = relationship("M2_SSD_SPECS", back_populates = "m2_ssdS")
    manufacturers:Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = "m2S")
    products:Mapped["Product"] = relationship("Product", back_populates = "m2_ssdS")
    baskets:Mapped["Basket"] = relationship("Basket", back_populates = "m2_ssdS")

class M2_SSD_SPECS(Base):
    __tablename__ = "M2_SSD_Specs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    frequency:Mapped[int] = mapped_column(Integer)
    tdp:Mapped[int] = mapped_column(Integer)
    speed_read:Mapped[int] = mapped_column(Integer)
    write_read:Mapped[int] = mapped_column(Integer)
    memory_id:Mapped[int] = mapped_column(Integer, ForeignKey("Memory_Sizes.id"))

    m2_ssdS:Mapped["M2_SSD"] = relationship("M2_SSD", back_populates = "specs")
    memories:Mapped["MemorySize"] = relationship("MemorySize", back_populates = "m2Specs")

class M2_SIZE(Base):
    __tablename__ = "M2_Sizes"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    size:Mapped[int] = mapped_column(Integer)

#размеры 2230, 2242, 2260, 2280
    m2SSD:Mapped["M2_SSD"] = relationship("M2_SSD", back_populates = "m2Size")
    motherboard_specs:Mapped["Motherboard_SPECS"] = relationship("Motherboard_SPECS", back_populates = "slots")



class SSD(Base):
    __tablename__ = "SSDs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))
    cost:Mapped[Numeric] = mapped_column(Numeric(10,2))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.SSD))
    image:Mapped[str] = mapped_column(String(255))
    ssd_specs_id:Mapped[int] = mapped_column(Integer, ForeignKey("SSD_Specs.id")) 


    products:Mapped["Product"] = relationship("Product", back_populates = "ssdS")
    specs:Mapped["SSD_SPECS"] = relationship("SSD_SPECS", back_populates = "ssdS")
    manufacturers:Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = "ssdS")
    baskets:Mapped["Basket"] = relationship("Basket", back_populates = "ssdS")


class SSD_SPECS(Base):
    __tablename__ = "SSD_Specs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    frequency:Mapped[int] = mapped_column(Integer)
    tdp:Mapped[int] = mapped_column(Integer)
    speed_read:Mapped[int] = mapped_column(Integer)
    write_read:Mapped[int] = mapped_column(Integer)
    memory_id:Mapped[int] = mapped_column(Integer, ForeignKey("Memory_Sizes.id"))


    ssdS:Mapped["SSD"] = relationship("SSD", back_populates = "specs")
    memories:Mapped["MemorySize"] = relationship("MemorySize", back_populates = "ssdSpecs")


class HDD(Base):
    __tablename__ = "HDDs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))
    cost:Mapped[Numeric] = mapped_column(Numeric(10,2))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.HDD))
    image:Mapped[str] = mapped_column(String(255))
    hdd_specs_id:Mapped[int] = mapped_column(Integer, ForeignKey("HDD_Specs.id"))

    products:Mapped["Product"] = relationship("Product", back_populates = "hddS")
    manufacturers:Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = "hddS")
    specs:Mapped["HDD_SPECS"] = relationship("HDD_SPECS", back_populates = "hddS")
    baskets:Mapped["Basket"] = relationship("Basket", back_populates = "hddS")

class HDD_SPECS(Base):
    __tablename__ = "HDD_Specs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    frequency:Mapped[int] = mapped_column(Integer)
    tdp:Mapped[int] = mapped_column(Integer)
    speed_read:Mapped[int] = mapped_column(Integer)
    write_read:Mapped[int] = mapped_column(Integer)
    memory_id:Mapped[int] = mapped_column(Integer, ForeignKey("Memory_Sizes.id"))

    hddS:Mapped["HDD"] = relationship("HDD", back_populates = "specs")
    memories:Mapped["MemorySize"] = relationship("MemorySize", back_populates = "hddSpecs")

class Chipset(Base):
    __tablename__ = "Chipsets"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))

    specs:Mapped["Motherboard_SPECS"] = relationship("Motherboard_SPECS", back_populates = "chipsets")

class Socket(Base):
    __tablename__ = "Sockets"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))

    coolers_sockets:Mapped["Cooler_Socket"] = relationship("Cooler_Socket", back_populates = "sockets")
    cpus_specs:Mapped["CPU_SPECS"] = relationship("CPU_SPECS", back_populates = "sockets")
    specs:Mapped["Motherboard_SPECS"] = relationship("Motherboard_SPECS", back_populates = "sockets")

class FormFactor(Base):
    __tablename__ = "FormFactors"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))

    specs:Mapped["Motherboard_SPECS"] = relationship("Motherboard_SPECS", back_populates = "forms")
    cases:Mapped["PC_CASE"] = relationship("PC_CASE", back_populates = "forms")

class PC_CASE(Base):
    __tablename__ = "PC_Cases"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))
    cost:Mapped[Numeric] = mapped_column(Numeric(10,2))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.CASE))
    image:Mapped[str] = mapped_column(String(255))
    pc_case_specs_id:Mapped[int] = mapped_column(Integer, ForeignKey('PC_Case_Specs.id'))
    form_factor_id:Mapped[int] = mapped_column(Integer, ForeignKey("FormFactors.id"))
    

    products:Mapped["Product"] = relationship("Product", back_populates = "cases")
    specs:Mapped["PC_CASE_SPECS"] = relationship("PC_CASE_SPECS", back_populates = "cases")
    manufacturers:Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = "cases")
    forms:Mapped["FormFactor"] = relationship("FormFactor", back_populates = "cases")
    baskets:Mapped["Basket"] = relationship("Basket", back_populates = "cases")


class PC_CASE_SPECS(Base):
    __tablename__ = "PC_Case_Specs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    weight:Mapped[Numeric] = mapped_column(Numeric(10,2))
    height:Mapped[Numeric] = mapped_column(Numeric(10,2))
    wight:Mapped[Numeric] = mapped_column(Numeric(10,2))
    case_type:Mapped[int] = mapped_column(Integer, ForeignKey("Case_Type.id"))
    front_vents_count:Mapped[int] = mapped_column(Integer)
    rear_vents_count:Mapped[int] = mapped_column(Integer)
    vent_size:Mapped[int] = mapped_column(Integer, ForeignKey("Vent_Size.id"))
    
    cases:Mapped["PC_CASE"] = relationship("PC_CASE", back_populates = "specs")
    sizes:Mapped["VENT_SIZE"] = relationship("VENT_SIZE", back_populates = "cases_specs")
    types:Mapped["CASE_TYPE"] = relationship("CASE_TYPE", back_populates = "cases_specs")


class CASE_TYPE(Base):
    __tablename__ = "Case_Type"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    

    cases_specs:Mapped["PC_CASE_SPECS"] = relationship("PC_CASE_SPECS", back_populates = "types")


class VENT_SIZE(Base):
    __tablename__ = 'Vent_Size'
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    size:Mapped[int] = mapped_column(Integer)
# 120mm, 92mm, 80mm, 70mm, 60mm, 40mm
    cases_specs:Mapped["PC_CASE_SPECS"] = relationship("PC_CASE_SPECS", back_populates = "sizes")


class Cooler(Base):
    __tablename__ = "Coolers"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String)
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))
    cooler_specs_id:Mapped[int] = mapped_column(Integer, ForeignKey("Coolers_Specs.id"))
    cost:Mapped[Numeric] = mapped_column(Numeric(10,2))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.TOWER))
    image:Mapped[str] = mapped_column(String(255))

    products:Mapped["Product"] = relationship("Product", back_populates = "coolers")
    coolers_sockets:Mapped["Cooler_Socket"] = relationship("Cooler_Socket", back_populates = "coolers")
    specs:Mapped["Cooler_Specs"] = relationship("Cooler_Specs", back_populates = "coolers")
    manufacturers:Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = "coolers")
    baskets:Mapped["Basket"] = relationship("Basket", back_populates = "coolers")



class Cooler_Specs(Base):
    __tablename__ = "Coolers_Specs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    base_material_id:Mapped[int] = mapped_column(Integer, ForeignKey("Materials.id"))
    radiator_material_id:Mapped[int] = mapped_column(Integer, ForeignKey("Materials.id"))

    coolers:Mapped["Cooler"] = relationship("Cooler", back_populates = "specs")
    base_material:Mapped["Material"] = relationship("Material", foreign_keys = [base_material_id], back_populates = "cooler_specs_base")
    radiator_material:Mapped["Material"] = relationship("Material", foreign_keys = [radiator_material_id], back_populates = "cooler_specs_radiator")


class Material(Base):
    __tablename__ = "Materials"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    material:Mapped[str] = mapped_column(String(50))
# записи по типу аллюминий/медь, медь, аллюминий и тд
    cooler_specs_base:Mapped["Cooler_Specs"] = relationship("Cooler_Specs", foreign_keys = "Cooler_Specs.base_material_id", back_populates = "base_material")
    cooler_specs_radiator:Mapped["Cooler_Specs"] = relationship("Cooler_Specs", foreign_keys = "Cooler_Specs.radiator_material_id", back_populates = "radiator_material")


class Cooler_Socket(Base):
    __tablename__ = "Coolers_Sockets"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    cooler_id:Mapped[int] = mapped_column(Integer, ForeignKey("Coolers.id"))
    socket_id:Mapped[int] = mapped_column(Integer, ForeignKey("Sockets.id"))


    coolers:Mapped["Cooler"] = relationship("Cooler", back_populates = "coolers_sockets")
    sockets:Mapped["Socket"] = relationship("Socket", back_populates = "coolers_sockets")



class VENT(Base):
    __tablename__ = "Vents"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.VENT))
    cost:Mapped[Numeric] = mapped_column(Numeric(10,2))
    image:Mapped[str] = mapped_column(String(255))
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))


    manufacturers:Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = 'vents')
    specs:Mapped["VENT_SPECS"] = relationship("VENT_SPECS", back_populates = "vents")



class VENT_SPECS(Base):
    __tablename__ = "Vents_Specs"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    vent_id:Mapped[int] = mapped_column(Integer, ForeignKey("Vents.id"))
    max_speed_rotation:Mapped[int] = mapped_column(Integer)
    min_speed_rotation:Mapped[int] = mapped_column(Integer)
    max_level_noise:Mapped[Numeric] = mapped_column(Numeric(10,2))

    vents:Mapped["VENT"] = relationship("VENT", back_populates = "specs")



class POWER_UNIT(Base):
    __tablename__ = "Power_Units"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    power:Mapped[int] = mapped_column(Integer)
    article:Mapped[str] = mapped_column(String(50), default = generate_articul(ItemsTypes.PU))
    image:Mapped[str] = mapped_column(String(255))
    certificate_id:Mapped[int] = mapped_column(Integer, ForeignKey("Certificates.id"))
    manufacturer_id:Mapped[int] = mapped_column(Integer, ForeignKey("Manufacturers.id"))


    certs:Mapped["Certificate"] = relationship("Certificate", back_populates = "units")
    manufacturers:Mapped["Manufacturer"] = relationship("Manufacturer", back_populates = "puS")
    products:Mapped["Product"] = relationship("Product", back_populates = "puS")
    baskets:Mapped["Basket"] = relationship("Basket", back_populates = "puS")

class Certificate(Base):
    __tablename__ = "Certificates"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    # бронзовый, серебрянный и тд

    units:Mapped["POWER_UNIT"] = relationship("POWER_UNIT", back_populates = "certs")

class Manufacturer(Base):
    __tablename__ = "Manufacturers"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    name:Mapped[str] = mapped_column(String(50))
    
    
    cpus:Mapped["CPU"] = relationship("CPU", back_populates = "manufacturers")
    gpus:Mapped["GPU"] = relationship("GPU", back_populates = "manufacturers")
    rams:Mapped["RAM"] = relationship("RAM", back_populates = "manufacturers")
    motherboards:Mapped["Motherboard"] = relationship("Motherboard", back_populates = 'manufacturers')
    m2S:Mapped["M2_SSD"] = relationship("M2_SSD", back_populates = "manufacturers")
    ssdS:Mapped["SSD"] = relationship("SSD", back_populates = "manufacturers")
    hddS:Mapped["HDD"] = relationship("HDD", back_populates = "manufacturers")
    cases:Mapped["PC_CASE"] = relationship("PC_CASE", back_populates = "manufacturers")
    vents:Mapped["VENT"] = relationship("VENT", back_populates = "manufacturers")
    coolers:Mapped["Cooler"] = relationship("Cooler", back_populates = "manufacturers")
    puS:Mapped["POWER_UNIT"] = relationship("POWER_UNIT", back_populates = "manufacturers")


class MemorySize(Base):
    __tablename__ = "Memory_Sizes"
    id:Mapped[int] = mapped_column(Integer, autoincrement = True, primary_key = True)
    size:Mapped[int] = mapped_column(Integer)
    #записи 120, 240, 256, 512, 1024, 2048 и тд

    m2Specs:Mapped["M2_SSD_SPECS"] = relationship("M2_SSD_SPECS", back_populates = "memories")
    ssdSpecs:Mapped["SSD_SPECS"] = relationship("SSD_SPECS", back_populates = "memories")
    hddSpecs:Mapped["HDD_SPECS"] = relationship("HDD_SPECS", back_populates  = "memories")
