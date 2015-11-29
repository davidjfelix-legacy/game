#![allow(dead_code)]

use std::rc::{Rc, Weak};
use entity::{Vec3f64, Entity};
mod coord;

struct Address {
    x: u64,
    y: u64,
    z: u64,
    depth: u8,
}

pub enum AddressLineage {
    Ancestor,
    Descendant,
    Sibling,
    Distant
}

struct Element {
    name: String,
}

pub enum ChunkOption {
    Local(Rc<LocalChunk>),
    Remote(Rc<RemoteChunk>)
}

pub enum ChildOption {
    Local(Rc<LocalChunk>),
    Remote(Rc<RemoteChunk>),
    None
}

pub enum ParentOption {
    Local(Weak<LocalChunk>),
    Remote(Rc<RemoteChunk>),
    None
}

pub struct LocalChunk {
    address: Address,
    center: Vec3f64,
    children: [ChildOption; 8],
    child_number: Option<u8>,
    entities: Vec<Rc<Entity>>,
    mass: f64,
    parent: ParentOption,
    scale: u8,
    structure: u64,
    summary: Rc<Element>,
}

pub struct RemoteChunk {
    connection: i32,
}

impl Address {
    fn from_string(address: String) -> Option<Address> {
        let mut xyz: (u64, u64, u64) = (1, 1, 1);
        let mut xyz_add: (u64, u64, u64);

        for (index, character) in address.chars().enumerate() {
            if index > 63 {
                break;
            }
            xyz_add =  match character.to_digit(8) {
                Some(0) => (0, 0, 0),
                Some(1) => (0, 0, 1),
                Some(2) => (0, 1, 0),
                Some(3) => (0, 1, 1),
                Some(4) => (1, 0, 0),
                Some(5) => (1, 0, 1),
                Some(6) => (1, 1, 0),
                Some(7) => (1, 1, 1),
                _ => return None,
            };
            xyz = (xyz.0 << 1, xyz.1 << 1, xyz.2 << 1);
            xyz = (xyz.0 + xyz_add.0, xyz.1 + xyz_add.1, xyz.2 + xyz_add.2);
        }
        Some(Address {x: xyz.0, y: xyz.1, z: xyz.2, depth: address.len() as u8})
    }
}

impl PartialEq for Address {
    fn eq(&self, other: &Self) -> bool {
        (((self.x == other.x) && (self.y == other.y)) && (self.z == other.z))
    }
}


pub trait Chunk {
    fn get_child(&self, x: u8, y: u8, z: u8) -> ChildOption;
    fn tick(&self, time_delta: f64);
}

impl Chunk for LocalChunk {
    fn get_child(&self, x: u8, y: u8, z: u8) -> ChildOption {

        let index = match (x, y, z) {
            (0, 0, 0) => Some(0),
            (0, 0, 1) => Some(1),
            (0, 1, 0) => Some(2),
            (0, 1, 1) => Some(3),
            (1, 0, 0) => Some(4),
            (1, 0, 1) => Some(5),
            (1, 1, 0) => Some(6),
            (1, 1, 1) => Some(7),
            _ => None,
        };

        match index {
            Some(i) => match self.children[i] {
                ChildOption::Local(ref chunk) => ChildOption::Local(chunk.clone()),
                ChildOption::Remote(ref chunk) => ChildOption::Remote(chunk.clone()),
                ChildOption::None => ChildOption::None
            },
            None => ChildOption::None
        }
    }

    fn tick(&self, time_delta: f64) {
    }
}

impl Chunk for RemoteChunk {
    fn get_child(&self, x: u8, y: u8, z: u8) -> ChildOption {
        ChildOption::None
    }
    fn tick (&self, time_delta: f64) {
    }
}

