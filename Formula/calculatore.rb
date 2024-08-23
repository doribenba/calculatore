class Calculatore < Formula
  desc "A simple command-line (Italian) calculator"
  homepage "https://github.com/doribenba/calculatore.git"  # Replace with your actual homepage URL if applicable
  url "file:///Users/dorian/calculator/calculatore-1.0.0.tar.gz"  # Update with your tarball path
  sha256 "d4b230805d0a8a5495afc39d2c79eb8b1bfbfdc1fc69e8f4c330843730c8d6b3"  # Replace with the SHA256 checksum you obtained

  def install
    bin.install "calculatore"
  end

  test do
    system "#{bin}/calculatore", "--help"
  end
end
