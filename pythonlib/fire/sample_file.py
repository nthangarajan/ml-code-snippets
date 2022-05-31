import fire

def sample_method():
    pass

def main():
    fire.Fire({
      'sample_method': sample_method,
      })

if __name__ == '__main__':
    main()